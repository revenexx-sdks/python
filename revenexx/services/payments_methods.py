from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..enums.payment_method_kind import PaymentMethodKind;
from ..enums.payment_fee_type import PaymentFeeType;
from ..models.error import Error;

class PaymentsMethods(Service):

    def __init__(self, client) -> None:
        super(PaymentsMethods, self).__init__(client)

    def payments_methods_list(
        self,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None,
        code: Optional[str] = None,
        kind: Optional[PaymentMethodKind] = None,
        enabled: Optional[bool] = None,
        provider: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Every method this tenant has configured, enabled or not — what the Cockpit's Payment methods screen shows and how an integration finds out which codes exist. It answers CONFIGURATION, never an offer: nothing here is evaluated against a buyer, so a method restricted to Germany, one whose order-value bounds exclude this basket and one whose PSP was never set up all come back the same way. The call a checkout makes is POST /payments/methods/eligible. Rows come back in whatever order the database returns them, so a storefront-shaped list needs `?order=position.asc` — `position` is the merchant's intended sequence and nothing sorts by it here on its own.

        Parameters
        ----------
        limit : Optional[float]
            Page size (default 50, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. Anything else is refused with 400.
        code : Optional[str]
            Exact method code.
        kind : Optional[PaymentMethodKind]
            Restrict to self-managed or PSP-backed methods.
        enabled : Optional[bool]
            Restrict to enabled or disabled methods. Indexed.
        provider : Optional[str]
            Exact PSP code.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/methods'
        api_params = {}

        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)
        if code is not None:
            api_params['code'] = self._normalize_value(code)
        if kind is not None:
            api_params['kind'] = self._normalize_value(kind)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if provider is not None:
            api_params['provider'] = self._normalize_value(provider)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def payments_methods_create(
        self,
        code: str,
        name: str,
        countries: Optional[List[str]] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        fee_amount: Optional[float] = None,
        fee_currency: Optional[str] = None,
        fee_type: Optional[PaymentFeeType] = None,
        kind: Optional[PaymentMethodKind] = None,
        labels: Optional[Dict[str, Any]] = None,
        max_order_value: Optional[float] = None,
        metadata: Optional[Dict[str, Any]] = None,
        min_order_value: Optional[float] = None,
        position: Optional[float] = None,
        provider: Optional[str] = None,
        provider_method: Optional[str] = None
    ) -> Error:
        """
        Adds a line a checkout can offer. A create cannot omit `code` and `name`; every other column is optional or defaulted by the database. Two rows of this tenant may not share `code` — that is the 409. Two defaults are worth knowing before the first call: `enabled` is false, so a new method reaches no checkout until it is switched on, and `kind` is 'self_managed' — a card or wallet method needs `kind: "psp"` plus a `provider` the catalog carries, or it falls back to the tenant's `default_provider` at payment time and fails there if none is set. The `code` is the value every payment, every checkout and every ERP will name this method by from now on, and once a single payment has been made under it a rename is refused with 409: choose it once.

        Parameters
        ----------
        code : str
            The machine name of the method, unique per tenant and lower case by convention ('invoice', 'prepayment', 'card', 'paypal'). It is the string the checkout asks for, the string every payment stores, and therefore the one value here that cannot be changed freely: renaming it would leave the ledger naming something that no longer exists, so it is refused with 409 for as long as any payment names it. Required on create.
        name : str
            Operator-facing name, in the language the merchant administers in. What a buyer sees comes from `labels`. Required on create.
        countries : Optional[List[str]]
            Allowed ISO 3166-1 alpha-2 country codes, compared upper-cased against the buyer country. null or an empty list means unrestricted — the invoice method this app seeds is restricted to DE, which is why an eligibility call without a country sees it excluded.
        description : Optional[str]
            One line explaining the method where it is offered — payment terms, what happens after the order. Shown to the buyer, so it is the merchant's wording rather than the app's.
        enabled : Optional[bool]
            A disabled method is never eligible and never reaches a checkout. This is the switch an operator wants: deleting a method the ledger still names — or renaming its `code` — is refused with 409. Defaults to false, so a half-configured method cannot reach a checkout by accident.
        fee_amount : Optional[float]
            The surcharge this method costs the buyer, read as an amount or as a percentage depending on `fee_type`. Never negative — a discount for paying a certain way is not expressible here. Defaults to 0.
        fee_currency : Optional[str]
            ISO 4217 code a fixed fee is expressed in. The database bounds the length at three characters and nothing else, so lower case is stored as written. Defaults to EUR, and lower case is accepted here exactly as the handlers accept it.
        fee_type : Optional[PaymentFeeType]
            How `fee_amount` applies: 'none' (no surcharge), 'fixed' (that many units of `fee_currency`) or 'percent' (that share of the order amount). Defaults to 'none'.
        kind : Optional[PaymentMethodKind]
            Who moves the money. 'self_managed' — invoice, prepayment — means the merchant fulfils and reconciles it outside any PSP, and such a payment authorizes the moment it is created. 'psp' means a configured provider authorizes, captures and refunds it. Defaults to 'self_managed'; 'psp' needs a 'provider' to transact.
        labels : Optional[Dict[str, Any]]
            Buyer-facing names keyed by language tag — what a storefront shows instead of the operator-facing `name`. Free jsonb: the database constrains neither the tags nor the values, so a client reads the tag it wants and falls back to `en`.
        max_order_value : Optional[float]
            Largest order amount this method may be used for — the usual credit-risk cap on invoice and prepayment. null means no upper bound.
        metadata : Optional[Dict[str, Any]]
            Free-form merchant data carried on the configuration. This app never reads it — it is storage for the integrations that do (an ERP key for the method, a ledger account, a display hint).
        min_order_value : Optional[float]
            Smallest order amount this method may be used for — the usual guard against paying a €5 order by invoice. null means no lower bound.
        position : Optional[float]
            Sort order at checkout, ascending — the merchant's preferred payment method first. Defaults to 0.
        provider : Optional[str]
            The PSP code this method transacts through, from GET /payments/providers/catalog. Only meaningful for kind 'psp'; a PSP method that names none falls back to the tenant's `default_provider` setting. Must be a code GET /payments/providers/catalog carries.
        provider_method : Optional[str]
            The provider's own payment-method id ('card', 'paypal', 'sepa_debit') — what the driver is told to charge. Copied onto every payment created with this method as `metadata.provider_method`.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/methods'
        api_params = {}
        if code is None:
            raise RevenexxException('Missing required parameter: "code"')

        if name is None:
            raise RevenexxException('Missing required parameter: "name"')


        api_params['code'] = self._normalize_value(code)
        api_params['countries'] = self._normalize_value(countries)
        api_params['description'] = self._normalize_value(description)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if fee_amount is not None:
            api_params['fee_amount'] = self._normalize_value(fee_amount)
        if fee_currency is not None:
            api_params['fee_currency'] = self._normalize_value(fee_currency)
        if fee_type is not None:
            api_params['fee_type'] = self._normalize_value(fee_type)
        if kind is not None:
            api_params['kind'] = self._normalize_value(kind)
        api_params['labels'] = self._normalize_value(labels)
        api_params['max_order_value'] = self._normalize_value(max_order_value)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['min_order_value'] = self._normalize_value(min_order_value)
        api_params['name'] = self._normalize_value(name)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        api_params['provider'] = self._normalize_value(provider)
        api_params['provider_method'] = self._normalize_value(provider_method)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def payments_methods_defaults(
        self
    ) -> Dict[str, Any]:
        """
        Writes the four methods a shop starts with — invoice and prepayment as self-managed, card and PayPal routed at the mock PSP so a fresh install can complete a checkout end to end — together with the four provider rows behind them: the built-in mock plus Stripe, PayPal and Novalnet, the three connectors this app opens outbound. The app already runs this for itself when it is installed (it listens on app.installed), so calling the route is for the second time and after: a method someone deleted, or a row a later release added that an existing install never got. Stripe, PayPal and Novalnet arrive disabled, in test mode and without credentials — the operator fills those in — while the mock arrives enabled, because it moves no money. Re-running is safe by design: it never duplicates a row and never overwrites an existing one, so nothing an operator has set can be undone by calling it again. Only genuinely missing option keys (a logo added after the first install) are filled, and those rows are reported as "updated" rather than created.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/methods/defaults'
        api_params = {}

        response = self.client.call('post', api_path, {
        }, api_params)

        return response


    def payments_methods_eligible(
        self,
        amount: Optional[float] = None,
        country: Optional[str] = None,
        currency: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        The checkout's question — "what can THIS buyer pay with?" — answered server-side before any PSP is involved, so the storefront never renders a method the create would then refuse with 422. It evaluates the buyer context against every configured method: disabled, a country outside `countries`, an amount outside `min_order_value`/`max_order_value`. Restriction dimensions are ANDed and entries within one are ORed, and an empty dimension means unrestricted. Eligible methods come back sorted by `position` with their fee already computed for this amount; everything else lands in `excluded` with the reason in words, which is what makes a support question answerable. It reads only — nothing is written and no provider is called. Two things it does NOT check: whether the method's PSP is configured and enabled (a method whose provider is switched off is still offered here and fails at POST /payments — a provider a method names can no longer be deleted, which closes the other half of the same gap), and anything about the buyer beyond country and amount. A context that matches nothing is 200 with an empty `methods` list, never 404.

        Parameters
        ----------
        amount : Optional[float]
            The order amount the order-value bounds are checked against and the percentage fees are computed from. Defaults to 0, which excludes every method carrying a minimum. Nothing is written, so the ledger's own amount bound does not apply here.
        country : Optional[str]
            The buyer's ISO 3166-1 alpha-2 country code. A method restricted to countries is excluded without it — an unknown buyer sees only the unrestricted methods, which is the safe default and not a bug.
        currency : Optional[str]
            ISO 4217 code the amount is in, echoed onto every computed fee. Defaults to EUR. This app does no conversion: the fee comes back in the currency it was asked with.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/methods/eligible'
        api_params = {}

        api_params['amount'] = self._normalize_value(amount)
        api_params['country'] = self._normalize_value(country)
        api_params['currency'] = self._normalize_value(currency)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def payments_methods_delete(
        self,
        id: str
    ) -> Error:
        """
        payments.method_code is a CODE, not a foreign key: a payment records what happened and has to survive the configuration it was made with. The cost of that looseness is that deleting a method turns every payment made with it into a row naming something that no longer exists. So the count is taken HERE and answered as 409 with the number, rather than left to whoever is about to click delete — a client that pre-counts asks a second question whose answer disagrees the moment a payment lands between the two calls. Disabling the method (enabled: false) is what an operator usually meant and stays available.

        Parameters
        ----------
        id : str
            The payment method configuration. A uuid — the data plane casts this segment and answers 400, not 404, for anything else.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/methods/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def payments_methods_get(
        self,
        id: str
    ) -> Error:
        """
        One configuration, every column, addressed by its row id — the edit form's read. It is addressed by ID and there is no route that takes a `code`, which matters because the CODE is what a checkout, a payment and an ERP name a method by: to resolve one, filter the list (`GET /payments/methods?code=invoice`), which answers a page of at most one row because (tenant_id, code) is unique. Reading a method says nothing about whether a buyer may use it — that is POST /payments/methods/eligible — and nothing about whether its PSP can transact, which is under the provider configuration.

        Parameters
        ----------
        id : str
            The payment method configuration. A uuid — the data plane casts this segment and answers 400, not 404, for anything else.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/methods/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def payments_methods_update(
        self,
        id: str,
        code: Optional[str] = None,
        countries: Optional[List[str]] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        fee_amount: Optional[float] = None,
        fee_currency: Optional[str] = None,
        fee_type: Optional[PaymentFeeType] = None,
        kind: Optional[PaymentMethodKind] = None,
        labels: Optional[Dict[str, Any]] = None,
        max_order_value: Optional[float] = None,
        metadata: Optional[Dict[str, Any]] = None,
        min_order_value: Optional[float] = None,
        name: Optional[str] = None,
        position: Optional[float] = None,
        provider: Optional[str] = None,
        provider_method: Optional[str] = None
    ) -> Error:
        """
        A PUT that PATCHES: only the keys in the body are written and every omitted column keeps its value, so `{"enabled": false}` is the whole request for taking a method out of checkout. A body with no writable key is refused with 400 rather than treated as a no-op. This is the route for all three things an operator changes about a method after it exists — the `enabled` switch that puts it in or out of checkout, the fee it charges (`fee_type`, `fee_amount`, `fee_currency`) and the restrictions that decide who is offered it (`countries`, `min_order_value`, `max_order_value`) — alongside its labels, description and `position`. `enabled: false` is the safe way to retire one — it disappears from POST /payments/methods/eligible immediately and stays on every payment ever made with it. The one write this route refuses is a rename of `code` while the ledger still names the old one. The three tables of this app carry no foreign keys at all: a payment names its method by `method_code` and its acquirer by `provider`, both plain text, because a payment records what happened and has to survive the configuration it was made with. So the database will not stop this — whatever the ledger still names, it goes on naming. A rename would therefore leave every recorded payment pointing at a code no configuration carries, which is the same harm DELETE on this row answers 409 for — so it answers the same 409, with the same `method_in_use` code and the same count. Renaming a method nothing has been paid with is still free, and so is every other column at any time.

        Parameters
        ----------
        id : str
            The payment method configuration. A uuid — the data plane casts this segment and answers 400, not 404, for anything else.
        code : Optional[str]
            The machine name of the method, unique per tenant and lower case by convention ('invoice', 'prepayment', 'card', 'paypal'). It is the string the checkout asks for, the string every payment stores, and therefore the one value here that cannot be changed freely: renaming it would leave the ledger naming something that no longer exists, so it is refused with 409 for as long as any payment names it. Required on create.
        countries : Optional[List[str]]
            Allowed ISO 3166-1 alpha-2 country codes, compared upper-cased against the buyer country. null or an empty list means unrestricted — the invoice method this app seeds is restricted to DE, which is why an eligibility call without a country sees it excluded.
        description : Optional[str]
            One line explaining the method where it is offered — payment terms, what happens after the order. Shown to the buyer, so it is the merchant's wording rather than the app's.
        enabled : Optional[bool]
            A disabled method is never eligible and never reaches a checkout. This is the switch an operator wants: deleting a method the ledger still names — or renaming its `code` — is refused with 409. Defaults to false, so a half-configured method cannot reach a checkout by accident.
        fee_amount : Optional[float]
            The surcharge this method costs the buyer, read as an amount or as a percentage depending on `fee_type`. Never negative — a discount for paying a certain way is not expressible here. Defaults to 0.
        fee_currency : Optional[str]
            ISO 4217 code a fixed fee is expressed in. The database bounds the length at three characters and nothing else, so lower case is stored as written. Defaults to EUR, and lower case is accepted here exactly as the handlers accept it.
        fee_type : Optional[PaymentFeeType]
            How `fee_amount` applies: 'none' (no surcharge), 'fixed' (that many units of `fee_currency`) or 'percent' (that share of the order amount). Defaults to 'none'.
        kind : Optional[PaymentMethodKind]
            Who moves the money. 'self_managed' — invoice, prepayment — means the merchant fulfils and reconciles it outside any PSP, and such a payment authorizes the moment it is created. 'psp' means a configured provider authorizes, captures and refunds it. Defaults to 'self_managed'; 'psp' needs a 'provider' to transact.
        labels : Optional[Dict[str, Any]]
            Buyer-facing names keyed by language tag — what a storefront shows instead of the operator-facing `name`. Free jsonb: the database constrains neither the tags nor the values, so a client reads the tag it wants and falls back to `en`.
        max_order_value : Optional[float]
            Largest order amount this method may be used for — the usual credit-risk cap on invoice and prepayment. null means no upper bound.
        metadata : Optional[Dict[str, Any]]
            Free-form merchant data carried on the configuration. This app never reads it — it is storage for the integrations that do (an ERP key for the method, a ledger account, a display hint).
        min_order_value : Optional[float]
            Smallest order amount this method may be used for — the usual guard against paying a €5 order by invoice. null means no lower bound.
        name : Optional[str]
            Operator-facing name, in the language the merchant administers in. What a buyer sees comes from `labels`. Required on create.
        position : Optional[float]
            Sort order at checkout, ascending — the merchant's preferred payment method first. Defaults to 0.
        provider : Optional[str]
            The PSP code this method transacts through, from GET /payments/providers/catalog. Only meaningful for kind 'psp'; a PSP method that names none falls back to the tenant's `default_provider` setting. Must be a code GET /payments/providers/catalog carries.
        provider_method : Optional[str]
            The provider's own payment-method id ('card', 'paypal', 'sepa_debit') — what the driver is told to charge. Copied onto every payment created with this method as `metadata.provider_method`.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/payments/methods/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if code is not None:
            api_params['code'] = self._normalize_value(code)
        api_params['countries'] = self._normalize_value(countries)
        api_params['description'] = self._normalize_value(description)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if fee_amount is not None:
            api_params['fee_amount'] = self._normalize_value(fee_amount)
        if fee_currency is not None:
            api_params['fee_currency'] = self._normalize_value(fee_currency)
        if fee_type is not None:
            api_params['fee_type'] = self._normalize_value(fee_type)
        if kind is not None:
            api_params['kind'] = self._normalize_value(kind)
        api_params['labels'] = self._normalize_value(labels)
        api_params['max_order_value'] = self._normalize_value(max_order_value)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['min_order_value'] = self._normalize_value(min_order_value)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        api_params['provider'] = self._normalize_value(provider)
        api_params['provider_method'] = self._normalize_value(provider_method)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)

