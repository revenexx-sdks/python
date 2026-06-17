from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.payment import Payment;
from ..enums.payment_fee_type import PaymentFeeType;
from ..enums.payment_method_kind import PaymentMethodKind;
from ..models.payment_method import PaymentMethod;
from ..models.payment_provider import PaymentProvider;

class Payments(Service):

    def __init__(self, client) -> None:
        super(Payments, self).__init__(client)

    def payments_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/payments'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def payments_create(
        self,
        amount: float,
        method_code: str,
        cart_id: Optional[str] = None,
        contact_id: Optional[str] = None,
        country: Optional[str] = None,
        currency: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        order_ref: Optional[str] = None,
        return_url: Optional[str] = None
    ) -> Payment:
        """
        

        Parameters
        ----------
        amount : float
            Order amount — 0 is legal (free orders), negative is not.
        method_code : str
            Code of a configured payment method.
        cart_id : Optional[str]
            The cart this payment pays for.
        contact_id : Optional[str]
            Paying customer contact.
        country : Optional[str]
            Buyer ISO country code for the eligibility check.
        currency : Optional[str]
            ISO 4217 code (default EUR).
        idempotency_key : Optional[str]
            Same key answers the same payment instead of a duplicate.
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        order_ref : Optional[str]
            External order reference — also the webhook fallback key.
        return_url : Optional[str]
            Where the PSP redirect flow returns the buyer to.
        
        Returns
        -------
        Payment
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/payments'
        api_params = {}
        if amount is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "amount"')

        if method_code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "method_code"')


        api_params['amount'] = self._normalize_value(amount)
        api_params['cart_id'] = self._normalize_value(cart_id)
        api_params['contact_id'] = self._normalize_value(contact_id)
        api_params['country'] = self._normalize_value(country)
        if currency is not None:
            api_params['currency'] = self._normalize_value(currency)
        api_params['idempotency_key'] = self._normalize_value(idempotency_key)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['method_code'] = self._normalize_value(method_code)
        api_params['order_ref'] = self._normalize_value(order_ref)
        api_params['return_url'] = self._normalize_value(return_url)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Payment)


    def payments_methods_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/payments/methods'
        api_params = {}

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
    ) -> PaymentMethod:
        """
        

        Parameters
        ----------
        code : str
            Stable method code (unique per tenant, e.g. 'invoice', 'card').
        name : str
            Display name.
        countries : Optional[List[str]]
            Allowed ISO country codes — empty/omitted = unrestricted.
        description : Optional[str]
            
        enabled : Optional[bool]
            Disabled methods are never eligible (default false).
        fee_amount : Optional[float]
            Fixed amount or percent value, per fee_type (default 0).
        fee_currency : Optional[str]
            ISO 4217 code (default EUR).
        fee_type : Optional[PaymentFeeType]
            How 'fee_amount' applies (default 'none').
        kind : Optional[PaymentMethodKind]
            Self-managed (merchant fulfils, default) or PSP-backed ('provider' required to transact).
        labels : Optional[Dict[str, Any]]
            Localized display names ({ de, en, … }).
        max_order_value : Optional[float]
            Maximum order amount — omitted = no upper bound.
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        min_order_value : Optional[float]
            Minimum order amount — omitted = no lower bound.
        position : Optional[float]
            Sort position in the checkout (default 0).
        provider : Optional[str]
            PSP code from the catalog — only for kind 'psp'.
        provider_method : Optional[str]
            The provider's payment method id (e.g. 'card', 'paypal').
        
        Returns
        -------
        PaymentMethod
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/payments/methods'
        api_params = {}
        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')

        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')


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

        return self._parse_response(response, model=PaymentMethod)


    def payments_methods_defaults(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
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
        

        Parameters
        ----------
        amount : Optional[float]
            Order amount the fees are computed against (default 0).
        country : Optional[str]
            Buyer ISO country code — methods with country restrictions need it.
        currency : Optional[str]
            ISO 4217 code (default EUR).
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
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
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/payments/methods/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def payments_methods_get(
        self,
        id: str
    ) -> PaymentMethod:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        PaymentMethod
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/payments/methods/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=PaymentMethod)


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
    ) -> PaymentMethod:
        """
        

        Parameters
        ----------
        id : str
            
        code : Optional[str]
            Stable method code (unique per tenant, e.g. 'invoice', 'card').
        countries : Optional[List[str]]
            Allowed ISO country codes — empty/omitted = unrestricted.
        description : Optional[str]
            
        enabled : Optional[bool]
            Disabled methods are never eligible (default false).
        fee_amount : Optional[float]
            Fixed amount or percent value, per fee_type (default 0).
        fee_currency : Optional[str]
            ISO 4217 code (default EUR).
        fee_type : Optional[PaymentFeeType]
            How 'fee_amount' applies (default 'none').
        kind : Optional[PaymentMethodKind]
            Self-managed (merchant fulfils, default) or PSP-backed ('provider' required to transact).
        labels : Optional[Dict[str, Any]]
            Localized display names ({ de, en, … }).
        max_order_value : Optional[float]
            Maximum order amount — omitted = no upper bound.
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        min_order_value : Optional[float]
            Minimum order amount — omitted = no lower bound.
        name : Optional[str]
            Display name.
        position : Optional[float]
            Sort position in the checkout (default 0).
        provider : Optional[str]
            PSP code from the catalog — only for kind 'psp'.
        provider_method : Optional[str]
            The provider's payment method id (e.g. 'card', 'paypal').
        
        Returns
        -------
        PaymentMethod
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/payments/methods/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

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

        return self._parse_response(response, model=PaymentMethod)


    def payments_providers_list(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/payments/providers'
        api_params = {}

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
    ) -> PaymentProvider:
        """
        

        Parameters
        ----------
        provider : str
            Provider code — must exist in the catalog (GET /payments/providers/catalog).
        credentials : Optional[Dict[str, Any]]
            PSP credentials — the catalog's credential_fields say which keys the auth scheme expects.
        enabled : Optional[bool]
            Only enabled providers transact (default false).
        name : Optional[str]
            Display name — defaults to the catalog label.
        options : Optional[Dict[str, Any]]
            Free-form provider options.
        test_mode : Optional[bool]
            Sandbox/test credentials (default true).
        webhook_secret : Optional[str]
            Shared secret for PSP callback verification.
        
        Returns
        -------
        PaymentProvider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/payments/providers'
        api_params = {}
        if provider is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider"')


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

        return self._parse_response(response, model=PaymentProvider)


    def payments_providers_catalog(
        self
    ) -> Dict[str, Any]:
        """
        

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
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
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/payments/providers/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def payments_providers_get(
        self,
        id: str
    ) -> PaymentProvider:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        PaymentProvider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/payments/providers/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=PaymentProvider)


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
    ) -> PaymentProvider:
        """
        

        Parameters
        ----------
        id : str
            
        credentials : Optional[Dict[str, Any]]
            PSP credentials — the catalog's credential_fields say which keys the auth scheme expects.
        enabled : Optional[bool]
            Only enabled providers transact (default false).
        name : Optional[str]
            Display name — defaults to the catalog label.
        options : Optional[Dict[str, Any]]
            Free-form provider options.
        provider : Optional[str]
            Provider code — must exist in the catalog (GET /payments/providers/catalog).
        test_mode : Optional[bool]
            Sandbox/test credentials (default true).
        webhook_secret : Optional[str]
            Shared secret for PSP callback verification.
        
        Returns
        -------
        PaymentProvider
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/payments/providers/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

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

        return self._parse_response(response, model=PaymentProvider)


    def payments_webhooks_ingest(
        self,
        provider: str,
        data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Consumes the dispatch envelope from webhooks.revenexx.com: normalizes the provider callback (stripe payment intents + a generic shape), resolves the payment by psp_payment_id or order_ref and moves the ledger. Facts only move forward — provider retries and redeliveries are idempotent no-ops; unverified envelopes are refused.

        Parameters
        ----------
        provider : str
            
        data : Dict[str, Any]
            Request body
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/payments/webhooks/{provider}'
        api_params = {}
        if provider is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "provider"')

        if data is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "data"')

        api_path = api_path.replace('{provider}', str(self._normalize_value(provider)))

        api_params['data'] = self._normalize_value(data)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def payments_get(
        self,
        id: str
    ) -> Payment:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Payment
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/payments/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Payment)


    def payments_cancel(
        self,
        id: str
    ) -> Payment:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Payment
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/payments/{id}/cancel'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=Payment)


    def payments_capture(
        self,
        id: str
    ) -> Payment:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Payment
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/payments/{id}/capture'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=Payment)


    def payments_confirm(
        self,
        id: str
    ) -> Payment:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Payment
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/payments/{id}/confirm'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=Payment)


    def payments_refund(
        self,
        id: str
    ) -> Payment:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Payment
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/payments/{id}/refund'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=Payment)

