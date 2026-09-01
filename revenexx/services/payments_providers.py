from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..models.error import Error;

class PaymentsProviders(Service):

    def __init__(self, client) -> None:
        super(PaymentsProviders, self).__init__(client)

    def payments_logos_get(
        self,
        slug: str
    ) -> Error:
        """
        Answers the SVG document for a catalog provider code (a shipped assets/logos/{code}.svg, otherwise a generated monogram tile), with content-type image/svg+xml and a one-day cache. It is the one route in this app that needs no tenant identity: the logos are bundled with the app rather than owned by anyone, so nothing here is tenant data and no key or tenant header is required to fetch one — which is what lets a storefront or a Cockpit screen point an <img> straight at it. Called directly on the app domain (https://revenexx-payments.apps.revenexx.io/payments/logos/stripe) the response carries its real content-type; through the gateway the body is passed through but labelled application/json, so use the app domain for <img> sources.

        Parameters
        ----------
        slug : str
            A catalog provider code, as GET /payments/providers/catalog lists it. Case-insensitive, and a trailing '.svg' is ignored. Not tenant data: the logos ship with the app and are identical for everyone.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/logos/{slug}'
        api_params = {}
        if slug is None:
            raise RevenexxException('Missing required parameter: "slug"')

        api_path = api_path.replace('{slug}', str(self._normalize_value(slug)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def payments_providers_list(
        self,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None,
        provider: Optional[str] = None,
        enabled: Optional[bool] = None,
        test_mode: Optional[bool] = None
    ) -> Dict[str, Any]:
        """
        PSP secrets are write-only: 'credentials' and 'webhook_secret' are accepted on create/update, stored for the drivers, and never returned by any route — the responses carry the public columns only (id, provider, name, enabled, test_mode, options, timestamps). To rotate a secret, write the new value; there is no way to read the current one back.

        Parameters
        ----------
        limit : Optional[float]
            Page size (default 50, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. Anything else is refused with 400.
        provider : Optional[str]
            Exact provider code.
        enabled : Optional[bool]
            Restrict to enabled or disabled providers.
        test_mode : Optional[bool]
            Restrict to sandbox or live configurations.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/providers'
        api_params = {}

        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)
        if provider is not None:
            api_params['provider'] = self._normalize_value(provider)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if test_mode is not None:
            api_params['test_mode'] = self._normalize_value(test_mode)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def payments_providers_create(
        self,
        provider: str,
        credentials: Optional[Dict[str, Any]] = None,
        enabled: Optional[bool] = None,
        name: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None,
        test_mode: Optional[bool] = None,
        webhook_secret: Optional[str] = None
    ) -> Error:
        """
        Activates one PSP account of this tenant. The `provider` code is not free text: it has to be one the catalog carries, and anything else is refused with 400 and a message listing the codes that are — so GET /payments/providers/catalog is the call that comes first, both for the code itself and for the credential field names this provider expects. PSP secrets are write-only: 'credentials' and 'webhook_secret' are accepted on create/update, stored for the drivers, and never returned by any route — the responses carry the public columns only (id, provider, name, enabled, test_mode, options, timestamps). To rotate a secret, write the new value; there is no way to read the current one back.

        Parameters
        ----------
        provider : str
            The catalog code of the PSP this row configures — one row per provider per tenant. GET /payments/providers/catalog lists every code that may appear here. It is what every payment and every method naming this PSP resolves it by, so changing it is refused with 409 for as long as one of them does. Required on create, and refused with 400 when the catalog does not carry it.
        credentials : Optional[Dict[str, Any]]
            The PSP's own API credentials, under the key names its auth scheme expects — `GET /payments/providers/catalog` publishes them per provider as `credential_fields` (Stripe: `api_key`; PayPal: `client_id` + `client_secret`; Novalnet: `api_key` + `payment_access_key` + `tariff_id`). They come from the provider's own dashboard, are handed to the driver in-process, and are never read back by any route. Write-only: to rotate one, write the new value. Whatever a document shows here is a placeholder.
        enabled : Optional[bool]
            Only an enabled provider takes NEW payments: a method pointing at a disabled one falls through to the tenant's `fallback_provider`, and to a 422 if there is none. Nothing else reads it — capture, cancel and refund on the payments this PSP already holds go on working — which is what makes disabling the safe retirement and deleting the refused one. Defaults to false — finish the credentials before switching it on.
        name : Optional[str]
            Operator-facing name of the configuration. Defaults to the catalog label, and is worth changing when a tenant runs two accounts with one PSP. null, omitted or empty falls back to the catalog label.
        options : Optional[Dict[str, Any]]
            Per-provider switches this app understands, plus anything the merchant keeps beside them. Three keys are the app's own: `logo_url` (the bundled logo, filled in when the provider is seeded), `capture_method` and `three_ds` (what the prism driver does today). Free jsonb — an unknown key is stored and ignored.
        test_mode : Optional[bool]
            Whether the driver talks to the PSP's sandbox. New configurations start in test mode: a provider nobody verified must not touch live money. Unstated takes the tenant's own `test_mode_default` setting.
        webhook_secret : Optional[str]
            The signing secret the PSP issues when its webhook endpoint is created, in the provider's own dashboard. webhooks.revenexx.com verifies each callback against it before the dispatcher hands the envelope to this app. Write-only, like `credentials`: it is stored, used, and never read back by any route, so there is nothing to compare a value against — to rotate it, write the new one. Whatever a document shows here is a generated placeholder, not a usable secret — writing it verbatim leaves every callback failing verification.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/providers'
        api_params = {}
        if provider is None:
            raise RevenexxException('Missing required parameter: "provider"')


        api_params['credentials'] = self._normalize_value(credentials)
        api_params['enabled'] = self._normalize_value(enabled)
        api_params['name'] = self._normalize_value(name)
        api_params['options'] = self._normalize_value(options)
        api_params['provider'] = self._normalize_value(provider)
        api_params['test_mode'] = self._normalize_value(test_mode)
        api_params['webhook_secret'] = self._normalize_value(webhook_secret)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def payments_providers_catalog(
        self
    ) -> Dict[str, Any]:
        """
        The closed set of `provider` codes POST /payments/providers accepts — anything else is refused with 400 and a message listing these. It runs to roughly thirty connectors, and each entry says which `driver` moves the money for it: nearly all of them go through the one connector layer this app embeds, hyperswitch-prism, with the built-in mock PSP alongside for demos and E2E. Read it to build the picker on an "add provider" form and to know what a credentials form has to ask for: `auth_type` is the scheme the connector authenticates with and `credential_fields` are the KEY NAMES to put inside `credentials` (never values, which come from the PSP's own dashboard). It says nothing about this tenant: no credential, no enabled flag, no test mode — that is GET /payments/providers. Watch `available`: a code with `false` has no driver in this deployment yet, so it can be created and stored and every transaction through it fails with `provider_unavailable`. The list is app-shipped and identical for everyone, so it is safe to cache hard and it changes only with a release of this app.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/providers/catalog'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def payments_providers_delete(
        self,
        id: str
    ) -> Error:
        """
        Removes the PSP account row and its stored secrets, once nothing depends on it any more. The three tables of this app carry no foreign keys at all: a payment names its method by `method_code` and its acquirer by `provider`, both plain text, because a payment records what happened and has to survive the configuration it was made with. So the database will not stop this — whatever the ledger still names, it goes on naming. So the database will not stop this and the count is taken HERE, exactly as DELETE /payments/methods/{id} takes it, and answered as one 409 carrying both numbers. Counted first: every payment still in a status a transition starts from — created, requires_action, authorized or captured — because capture, cancel and refund all resolve the provider BY CODE and would answer 422 `provider_not_configured` with the row gone, leaving an authorization that can neither be collected nor released and a captured payment that can no longer be refunded here at all. Counted second: every payment method naming this provider, because POST /payments/methods/eligible does not check providers, so a checkout would go on offering a method whose next POST /payments fails at authorization unless the tenant's `fallback_provider` names one that is still configured. What is deliberately NOT counted is a settled payment — failed, cancelled or refunded: no transition starts there, so nothing will ask this provider about it again, and a `provider` code is closed catalog data that goes on meaning Stripe or PayPal with no configuration behind it. The refusal names `enabled: false` because that is usually what was meant: a disabled provider stops taking NEW payments exactly as a deleted one does, and every transition on the payments it already holds keeps working, since only the create path asks whether it is enabled.

        Parameters
        ----------
        id : str
            The PSP configuration. A uuid — the data plane casts this segment and answers 400, not 404, for anything else.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/providers/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def payments_providers_get(
        self,
        id: str
    ) -> Error:
        """
        PSP secrets are write-only: 'credentials' and 'webhook_secret' are accepted on create/update, stored for the drivers, and never returned by any route — the responses carry the public columns only (id, provider, name, enabled, test_mode, options, timestamps). To rotate a secret, write the new value; there is no way to read the current one back.

        Parameters
        ----------
        id : str
            The PSP configuration. A uuid — the data plane casts this segment and answers 400, not 404, for anything else.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/providers/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def payments_providers_update(
        self,
        id: str,
        credentials: Optional[Dict[str, Any]] = None,
        enabled: Optional[bool] = None,
        name: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None,
        provider: Optional[str] = None,
        test_mode: Optional[bool] = None,
        webhook_secret: Optional[str] = None
    ) -> Error:
        """
        A partial write: omitted fields keep their value. Three things are changed here in practice — the `credentials` (and `webhook_secret`) when a key is rotated, `test_mode` when an account moves from the PSP's sandbox to live, and `enabled` when it is switched on or taken out of service. PSP secrets are write-only: 'credentials' and 'webhook_secret' are accepted on create/update, stored for the drivers, and never returned by any route — the responses carry the public columns only (id, provider, name, enabled, test_mode, options, timestamps). To rotate a secret, write the new value; there is no way to read the current one back. One field is not like the others: `provider` is the CODE every payment and every method resolves this PSP by, so writing a different one is the delete through another door and is refused with the same 409 while anything still names the current code. Switching acquirer is a second configuration plus `enabled: false` on this one, never a rename.

        Parameters
        ----------
        id : str
            The PSP configuration. A uuid — the data plane casts this segment and answers 400, not 404, for anything else.
        credentials : Optional[Dict[str, Any]]
            The PSP's own API credentials, under the key names its auth scheme expects — `GET /payments/providers/catalog` publishes them per provider as `credential_fields` (Stripe: `api_key`; PayPal: `client_id` + `client_secret`; Novalnet: `api_key` + `payment_access_key` + `tariff_id`). They come from the provider's own dashboard, are handed to the driver in-process, and are never read back by any route. Write-only: to rotate one, write the new value. Whatever a document shows here is a placeholder.
        enabled : Optional[bool]
            Only an enabled provider takes NEW payments: a method pointing at a disabled one falls through to the tenant's `fallback_provider`, and to a 422 if there is none. Nothing else reads it — capture, cancel and refund on the payments this PSP already holds go on working — which is what makes disabling the safe retirement and deleting the refused one. Defaults to false — finish the credentials before switching it on.
        name : Optional[str]
            Operator-facing name of the configuration. Defaults to the catalog label, and is worth changing when a tenant runs two accounts with one PSP. Written straight to the database, which refuses an empty one.
        options : Optional[Dict[str, Any]]
            Per-provider switches this app understands, plus anything the merchant keeps beside them. Three keys are the app's own: `logo_url` (the bundled logo, filled in when the provider is seeded), `capture_method` and `three_ds` (what the prism driver does today). Free jsonb — an unknown key is stored and ignored.
        provider : Optional[str]
            The catalog code of the PSP this row configures — one row per provider per tenant. GET /payments/providers/catalog lists every code that may appear here. It is what every payment and every method naming this PSP resolves it by, so changing it is refused with 409 for as long as one of them does. Required on create, and refused with 400 when the catalog does not carry it.
        test_mode : Optional[bool]
            Whether the driver talks to the PSP's sandbox. New configurations start in test mode: a provider nobody verified must not touch live money. Unstated takes the tenant's own `test_mode_default` setting.
        webhook_secret : Optional[str]
            The signing secret the PSP issues when its webhook endpoint is created, in the provider's own dashboard. webhooks.revenexx.com verifies each callback against it before the dispatcher hands the envelope to this app. Write-only, like `credentials`: it is stored, used, and never read back by any route, so there is nothing to compare a value against — to rotate it, write the new one. Whatever a document shows here is a generated placeholder, not a usable secret — writing it verbatim leaves every callback failing verification.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/providers/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['credentials'] = self._normalize_value(credentials)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        api_params['options'] = self._normalize_value(options)
        if provider is not None:
            api_params['provider'] = self._normalize_value(provider)
        if test_mode is not None:
            api_params['test_mode'] = self._normalize_value(test_mode)
        api_params['webhook_secret'] = self._normalize_value(webhook_secret)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)

