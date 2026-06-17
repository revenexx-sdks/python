from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..enums.shipping_method_matrix_basis import ShippingMethodMatrixBasis;
from ..enums.shipping_method_pricing_type import ShippingMethodPricingType;
from ..models.shipping_method import ShippingMethod;
from ..models.shipping_rate_tier import ShippingRateTier;
from ..models.shipping_rate_tier_replace_item import ShippingRateTierReplaceItem;

class Shipping(Service):

    def __init__(self, client) -> None:
        super(Shipping, self).__init__(client)

    def shipping_methods_list(
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

        api_path = '/v1/shipping/methods'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def shipping_methods_create(
        self,
        code: str,
        name: str,
        carrier: Optional[str] = None,
        countries: Optional[List[str]] = None,
        currency: Optional[str] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        eta_days_max: Optional[float] = None,
        eta_days_min: Optional[float] = None,
        free_above: Optional[float] = None,
        labels: Optional[Dict[str, Any]] = None,
        matrix_attribute: Optional[str] = None,
        matrix_basis: Optional[ShippingMethodMatrixBasis] = None,
        metadata: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        price: Optional[float] = None,
        pricing_type: Optional[ShippingMethodPricingType] = None
    ) -> ShippingMethod:
        """
        

        Parameters
        ----------
        code : str
            Stable method code, unique per tenant (e.g. standard, express).
        name : str
            Display name.
        carrier : Optional[str]
            Carrier anchor for the upcoming carrier connect (dynamic rates, tracking links).
        countries : Optional[List[str]]
            Allowed ISO 3166-1 alpha-2 codes; null or empty = worldwide.
        currency : Optional[str]
            ISO 4217 code (default EUR).
        description : Optional[str]
            
        enabled : Optional[bool]
            Only enabled methods appear in rate responses (default false).
        eta_days_max : Optional[float]
            Delivery-time estimate for the checkout (days, upper bound).
        eta_days_min : Optional[float]
            Delivery-time estimate for the checkout (days, lower bound).
        free_above : Optional[float]
            Free shipping at or above this order value — wins over every pricing model.
        labels : Optional[Dict[str, Any]]
            Localized display names keyed by locale (e.g. {de, en}).
        matrix_attribute : Optional[str]
            Attribute name for matrix_basis 'attribute'.
        matrix_basis : Optional[ShippingMethodMatrixBasis]
            The measure a matrix method prices over; 'attribute' reads matrix_attribute from the rate request.
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        position : Optional[float]
            Sort order in the checkout (default 0).
        price : Optional[float]
            The fixed price (default 0) — ignored for 'free' and 'matrix'.
        pricing_type : Optional[ShippingMethodPricingType]
            Pricing model (default 'fixed'): one price, no price, or tiered over a measure.
        
        Returns
        -------
        ShippingMethod
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/shipping/methods'
        api_params = {}
        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')

        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')


        api_params['carrier'] = self._normalize_value(carrier)
        api_params['code'] = self._normalize_value(code)
        api_params['countries'] = self._normalize_value(countries)
        if currency is not None:
            api_params['currency'] = self._normalize_value(currency)
        api_params['description'] = self._normalize_value(description)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        api_params['eta_days_max'] = self._normalize_value(eta_days_max)
        api_params['eta_days_min'] = self._normalize_value(eta_days_min)
        api_params['free_above'] = self._normalize_value(free_above)
        api_params['labels'] = self._normalize_value(labels)
        api_params['matrix_attribute'] = self._normalize_value(matrix_attribute)
        api_params['matrix_basis'] = self._normalize_value(matrix_basis)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['name'] = self._normalize_value(name)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if price is not None:
            api_params['price'] = self._normalize_value(price)
        if pricing_type is not None:
            api_params['pricing_type'] = self._normalize_value(pricing_type)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ShippingMethod)


    def shipping_methods_defaults(
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

        api_path = '/v1/shipping/methods/defaults'
        api_params = {}

        response = self.client.call('post', api_path, {
        }, api_params)

        return response


    def shipping_methods_delete(
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

        api_path = '/v1/shipping/methods/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def shipping_methods_get(
        self,
        id: str
    ) -> ShippingMethod:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        ShippingMethod
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/shipping/methods/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ShippingMethod)


    def shipping_methods_update(
        self,
        id: str,
        carrier: Optional[str] = None,
        code: Optional[str] = None,
        countries: Optional[List[str]] = None,
        currency: Optional[str] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        eta_days_max: Optional[float] = None,
        eta_days_min: Optional[float] = None,
        free_above: Optional[float] = None,
        labels: Optional[Dict[str, Any]] = None,
        matrix_attribute: Optional[str] = None,
        matrix_basis: Optional[ShippingMethodMatrixBasis] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        position: Optional[float] = None,
        price: Optional[float] = None,
        pricing_type: Optional[ShippingMethodPricingType] = None
    ) -> ShippingMethod:
        """
        

        Parameters
        ----------
        id : str
            
        carrier : Optional[str]
            Carrier anchor for the upcoming carrier connect (dynamic rates, tracking links).
        code : Optional[str]
            Stable method code, unique per tenant (e.g. standard, express).
        countries : Optional[List[str]]
            Allowed ISO 3166-1 alpha-2 codes; null or empty = worldwide.
        currency : Optional[str]
            ISO 4217 code (default EUR).
        description : Optional[str]
            
        enabled : Optional[bool]
            Only enabled methods appear in rate responses (default false).
        eta_days_max : Optional[float]
            Delivery-time estimate for the checkout (days, upper bound).
        eta_days_min : Optional[float]
            Delivery-time estimate for the checkout (days, lower bound).
        free_above : Optional[float]
            Free shipping at or above this order value — wins over every pricing model.
        labels : Optional[Dict[str, Any]]
            Localized display names keyed by locale (e.g. {de, en}).
        matrix_attribute : Optional[str]
            Attribute name for matrix_basis 'attribute'.
        matrix_basis : Optional[ShippingMethodMatrixBasis]
            The measure a matrix method prices over; 'attribute' reads matrix_attribute from the rate request.
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        name : Optional[str]
            Display name.
        position : Optional[float]
            Sort order in the checkout (default 0).
        price : Optional[float]
            The fixed price (default 0) — ignored for 'free' and 'matrix'.
        pricing_type : Optional[ShippingMethodPricingType]
            Pricing model (default 'fixed'): one price, no price, or tiered over a measure.
        
        Returns
        -------
        ShippingMethod
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/shipping/methods/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['carrier'] = self._normalize_value(carrier)
        if code is not None:
            api_params['code'] = self._normalize_value(code)
        api_params['countries'] = self._normalize_value(countries)
        if currency is not None:
            api_params['currency'] = self._normalize_value(currency)
        api_params['description'] = self._normalize_value(description)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        api_params['eta_days_max'] = self._normalize_value(eta_days_max)
        api_params['eta_days_min'] = self._normalize_value(eta_days_min)
        api_params['free_above'] = self._normalize_value(free_above)
        api_params['labels'] = self._normalize_value(labels)
        api_params['matrix_attribute'] = self._normalize_value(matrix_attribute)
        api_params['matrix_basis'] = self._normalize_value(matrix_basis)
        api_params['metadata'] = self._normalize_value(metadata)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if price is not None:
            api_params['price'] = self._normalize_value(price)
        if pricing_type is not None:
            api_params['pricing_type'] = self._normalize_value(pricing_type)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ShippingMethod)


    def shipping_tiers_list(
        self,
        method_id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        method_id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/shipping/methods/{method_id}/tiers'
        api_params = {}
        if method_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "method_id"')

        api_path = api_path.replace('{methodId}', str(self._normalize_value(method_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def shipping_tiers_create(
        self,
        method_id: str,
        from_value: Optional[float] = None,
        position: Optional[float] = None,
        price: Optional[float] = None
    ) -> ShippingRateTier:
        """
        

        Parameters
        ----------
        method_id : str
            
        from_value : Optional[float]
            Tier threshold (default 0) — the tier with the highest from_value at or below the measured value wins.
        position : Optional[float]
            Sort order (default 0; bulk replace derives it from the array index).
        price : Optional[float]
            Price of this tier (default 0).
        
        Returns
        -------
        ShippingRateTier
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/shipping/methods/{method_id}/tiers'
        api_params = {}
        if method_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "method_id"')

        api_path = api_path.replace('{methodId}', str(self._normalize_value(method_id)))

        if from_value is not None:
            api_params['from_value'] = self._normalize_value(from_value)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if price is not None:
            api_params['price'] = self._normalize_value(price)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ShippingRateTier)


    def shipping_tiers_replace(
        self,
        method_id: str,
        tiers: List[ShippingRateTierReplaceItem]
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        method_id : str
            
        tiers : List[ShippingRateTierReplaceItem]
            The complete new tier set (set semantics) — positions are derived from the array order.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/shipping/methods/{method_id}/tiers'
        api_params = {}
        if method_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "method_id"')

        if tiers is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "tiers"')

        api_path = api_path.replace('{methodId}', str(self._normalize_value(method_id)))

        api_params['tiers'] = self._normalize_value(tiers)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def shipping_tiers_delete(
        self,
        method_id: str,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        method_id : str
            
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

        api_path = '/v1/shipping/methods/{method_id}/tiers/{id}'
        api_params = {}
        if method_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "method_id"')

        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{methodId}', str(self._normalize_value(method_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def shipping_tiers_get(
        self,
        method_id: str,
        id: str
    ) -> ShippingRateTier:
        """
        

        Parameters
        ----------
        method_id : str
            
        id : str
            
        
        Returns
        -------
        ShippingRateTier
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/shipping/methods/{method_id}/tiers/{id}'
        api_params = {}
        if method_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "method_id"')

        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{methodId}', str(self._normalize_value(method_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ShippingRateTier)


    def shipping_tiers_update(
        self,
        method_id: str,
        id: str,
        from_value: Optional[float] = None,
        position: Optional[float] = None,
        price: Optional[float] = None
    ) -> ShippingRateTier:
        """
        

        Parameters
        ----------
        method_id : str
            
        id : str
            
        from_value : Optional[float]
            Tier threshold (default 0) — the tier with the highest from_value at or below the measured value wins.
        position : Optional[float]
            Sort order (default 0; bulk replace derives it from the array index).
        price : Optional[float]
            Price of this tier (default 0).
        
        Returns
        -------
        ShippingRateTier
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/shipping/methods/{method_id}/tiers/{id}'
        api_params = {}
        if method_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "method_id"')

        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{methodId}', str(self._normalize_value(method_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if from_value is not None:
            api_params['from_value'] = self._normalize_value(from_value)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if price is not None:
            api_params['price'] = self._normalize_value(price)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ShippingRateTier)


    def shipping_rates(
        self,
        attributes: Optional[Dict[str, Any]] = None,
        country: Optional[str] = None,
        currency: Optional[str] = None,
        market_id: Optional[str] = None,
        order_value: Optional[float] = None,
        quantity: Optional[float] = None,
        weight: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        attributes : Optional[Dict[str, Any]]
            Measure values for attribute matrices, keyed by attribute name.
        country : Optional[str]
            Destination ISO 3166-1 alpha-2 code — checked against method country restrictions.
        currency : Optional[str]
            Echoed into the rates (default 'EUR').
        market_id : Optional[str]
            Buyer market for tax resolution (else inferred from country, else first market).
        order_value : Optional[float]
            Order value (default 0) — drives free-above thresholds and order_value matrices.
        quantity : Optional[float]
            Total quantity — measure for quantity matrices.
        weight : Optional[float]
            Total weight — measure for weight matrices.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/shipping/rates'
        api_params = {}

        api_params['attributes'] = self._normalize_value(attributes)
        api_params['country'] = self._normalize_value(country)
        api_params['currency'] = self._normalize_value(currency)
        api_params['market_id'] = self._normalize_value(market_id)
        api_params['order_value'] = self._normalize_value(order_value)
        api_params['quantity'] = self._normalize_value(quantity)
        api_params['weight'] = self._normalize_value(weight)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response

