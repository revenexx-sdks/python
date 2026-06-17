from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.cart import Cart;
from ..enums.cart_io_direction import CartIoDirection;
from ..enums.cart_io_apply_mode import CartIoApplyMode;
from ..enums.cart_io_entity import CartIoEntity;
from ..enums.cart_io_format import CartIoFormat;
from ..models.io_profile import IoProfile;
from ..enums.cart_item_type import CartItemType;
from ..models.cart_item import CartItem;
from ..models.cart_item_create_request import CartItemCreateRequest;
from ..enums.cart_export_format import CartExportFormat;

class Carts(Service):

    def __init__(self, client) -> None:
        super(Carts, self).__init__(client)

    def carts_list(
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

        api_path = '/v1/carts'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def carts_create(
        self,
        channel_id: Optional[str] = None,
        contact_id: Optional[str] = None,
        currency: Optional[str] = None,
        is_current: Optional[bool] = None,
        market_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        session_key: Optional[str] = None
    ) -> Cart:
        """
        

        Parameters
        ----------
        channel_id : Optional[str]
            
        contact_id : Optional[str]
            Owning customer contact.
        currency : Optional[str]
            ISO 4217 code (default EUR).
        is_current : Optional[bool]
            Make this THE current cart of its owner.
        market_id : Optional[str]
            
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        name : Optional[str]
            Display name (default 'Cart').
        session_key : Optional[str]
            Owning guest session.
        
        Returns
        -------
        Cart
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts'
        api_params = {}

        api_params['channel_id'] = self._normalize_value(channel_id)
        api_params['contact_id'] = self._normalize_value(contact_id)
        api_params['currency'] = self._normalize_value(currency)
        api_params['is_current'] = self._normalize_value(is_current)
        api_params['market_id'] = self._normalize_value(market_id)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['name'] = self._normalize_value(name)
        api_params['session_key'] = self._normalize_value(session_key)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Cart)


    def carts_claim(
        self,
        contact_id: str,
        session_key: str,
        target_cart_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        contact_id : str
            Contact taking ownership.
        session_key : str
            Guest session whose active carts are handed over.
        target_cart_id : Optional[str]
            Merge the session carts into this cart instead of adopting them.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts/claim'
        api_params = {}
        if contact_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "contact_id"')

        if session_key is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "session_key"')


        api_params['contact_id'] = self._normalize_value(contact_id)
        api_params['session_key'] = self._normalize_value(session_key)
        api_params['target_cart_id'] = self._normalize_value(target_cart_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def carts_import(
        self,
        contact_id: Optional[str] = None,
        csv: Optional[str] = None,
        name: Optional[str] = None,
        payload: Optional[Dict[str, Any]] = None,
        profile_id: Optional[str] = None,
        session_key: Optional[str] = None,
        target_cart_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        contact_id : Optional[str]
            Owner of a newly created cart.
        csv : Optional[str]
            Raw CSV content (alternative to payload for csv profiles).
        name : Optional[str]
            Name for a newly created cart.
        payload : Optional[Dict[str, Any]]
            The import payload: '{cart, items}' object, or a raw JSON/CSV string in the profile's format.
        profile_id : Optional[str]
            Import profile to run; ad-hoc import when omitted.
        session_key : Optional[str]
            Guest owner of a newly created cart.
        target_cart_id : Optional[str]
            Existing active cart to import into.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts/import'
        api_params = {}

        api_params['contact_id'] = self._normalize_value(contact_id)
        if csv is not None:
            api_params['csv'] = self._normalize_value(csv)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if payload is not None:
            api_params['payload'] = self._normalize_value(payload)
        api_params['profile_id'] = self._normalize_value(profile_id)
        if session_key is not None:
            api_params['session_key'] = self._normalize_value(session_key)
        api_params['target_cart_id'] = self._normalize_value(target_cart_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def carts_io_profiles_list(
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

        api_path = '/v1/carts/io/profiles'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def carts_io_profiles_create(
        self,
        direction: CartIoDirection,
        name: str,
        apply_mode: Optional[CartIoApplyMode] = None,
        entity: Optional[CartIoEntity] = None,
        format: Optional[CartIoFormat] = None,
        is_template: Optional[bool] = None,
        mapping: Optional[Dict[str, Any]] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> IoProfile:
        """
        

        Parameters
        ----------
        direction : CartIoDirection
            
        name : str
            
        apply_mode : Optional[CartIoApplyMode]
            Default 'insert'.
        entity : Optional[CartIoEntity]
            Default 'carts'.
        format : Optional[CartIoFormat]
            Default 'json'.
        is_template : Optional[bool]
            
        mapping : Optional[Dict[str, Any]]
            Column mapping (Baseline-IO-compatible).
        options : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        IoProfile
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts/io/profiles'
        api_params = {}
        if direction is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "direction"')

        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')


        if apply_mode is not None:
            api_params['apply_mode'] = self._normalize_value(apply_mode)
        api_params['direction'] = self._normalize_value(direction)
        if entity is not None:
            api_params['entity'] = self._normalize_value(entity)
        if format is not None:
            api_params['format'] = self._normalize_value(format)
        if is_template is not None:
            api_params['is_template'] = self._normalize_value(is_template)
        if mapping is not None:
            api_params['mapping'] = self._normalize_value(mapping)
        api_params['name'] = self._normalize_value(name)
        if options is not None:
            api_params['options'] = self._normalize_value(options)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=IoProfile)


    def carts_io_profiles_defaults(
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

        api_path = '/v1/carts/io/profiles/defaults'
        api_params = {}

        response = self.client.call('post', api_path, {
        }, api_params)

        return response


    def carts_io_profiles_delete(
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

        api_path = '/v1/carts/io/profiles/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def carts_io_profiles_get(
        self,
        id: str
    ) -> IoProfile:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        IoProfile
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts/io/profiles/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=IoProfile)


    def carts_io_profiles_update(
        self,
        id: str,
        apply_mode: Optional[CartIoApplyMode] = None,
        direction: Optional[CartIoDirection] = None,
        entity: Optional[CartIoEntity] = None,
        format: Optional[CartIoFormat] = None,
        is_template: Optional[bool] = None,
        mapping: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> IoProfile:
        """
        

        Parameters
        ----------
        id : str
            
        apply_mode : Optional[CartIoApplyMode]
            Default 'insert'.
        direction : Optional[CartIoDirection]
            
        entity : Optional[CartIoEntity]
            Default 'carts'.
        format : Optional[CartIoFormat]
            Default 'json'.
        is_template : Optional[bool]
            
        mapping : Optional[Dict[str, Any]]
            Column mapping (Baseline-IO-compatible).
        name : Optional[str]
            
        options : Optional[Dict[str, Any]]
            
        
        Returns
        -------
        IoProfile
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts/io/profiles/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if apply_mode is not None:
            api_params['apply_mode'] = self._normalize_value(apply_mode)
        if direction is not None:
            api_params['direction'] = self._normalize_value(direction)
        if entity is not None:
            api_params['entity'] = self._normalize_value(entity)
        if format is not None:
            api_params['format'] = self._normalize_value(format)
        if is_template is not None:
            api_params['is_template'] = self._normalize_value(is_template)
        if mapping is not None:
            api_params['mapping'] = self._normalize_value(mapping)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if options is not None:
            api_params['options'] = self._normalize_value(options)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=IoProfile)


    def carts_merge(
        self,
        source_cart_id: str,
        target_cart_id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        source_cart_id : str
            Cart whose lines move into the target (becomes status merged).
        target_cart_id : str
            Receiving cart (must be active).
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts/merge'
        api_params = {}
        if source_cart_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "source_cart_id"')

        if target_cart_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "target_cart_id"')


        api_params['source_cart_id'] = self._normalize_value(source_cart_id)
        api_params['target_cart_id'] = self._normalize_value(target_cart_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def carts_items_list(
        self,
        cart_id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        cart_id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts/{cart_id}/items'
        api_params = {}
        if cart_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "cart_id"')

        api_path = api_path.replace('{cartId}', str(self._normalize_value(cart_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def carts_items_create(
        self,
        cart_id: str,
        configuration: Optional[Dict[str, Any]] = None,
        currency: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        position: Optional[float] = None,
        product_id: Optional[str] = None,
        quantity: Optional[float] = None,
        sku: Optional[str] = None,
        snapshot: Optional[Dict[str, Any]] = None,
        tax_rate: Optional[float] = None,
        type: Optional[CartItemType] = None,
        unit: Optional[str] = None,
        unit_price: Optional[float] = None
    ) -> CartItem:
        """
        

        Parameters
        ----------
        cart_id : str
            
        configuration : Optional[Dict[str, Any]]
            Free-form configuration — configured lines never merge.
        currency : Optional[str]
            Defaults to the cart's currency.
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        name : Optional[str]
            Falls back to 'sku' when omitted.
        position : Optional[float]
            
        product_id : Optional[str]
            
        quantity : Optional[float]
            Default 1.
        sku : Optional[str]
            
        snapshot : Optional[Dict[str, Any]]
            Loose product snapshot at add-time (price, name, image, …).
        tax_rate : Optional[float]
            
        type : Optional[CartItemType]
            Line type (default 'product'). Plain product lines merge by product+price; configurations always stand alone.
        unit : Optional[str]
            
        unit_price : Optional[float]
            Per-unit net price — line_total is always derived.
        
        Returns
        -------
        CartItem
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts/{cart_id}/items'
        api_params = {}
        if cart_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "cart_id"')

        api_path = api_path.replace('{cartId}', str(self._normalize_value(cart_id)))

        api_params['configuration'] = self._normalize_value(configuration)
        api_params['currency'] = self._normalize_value(currency)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['name'] = self._normalize_value(name)
        api_params['position'] = self._normalize_value(position)
        api_params['product_id'] = self._normalize_value(product_id)
        api_params['quantity'] = self._normalize_value(quantity)
        api_params['sku'] = self._normalize_value(sku)
        api_params['snapshot'] = self._normalize_value(snapshot)
        api_params['tax_rate'] = self._normalize_value(tax_rate)
        if type is not None:
            api_params['type'] = self._normalize_value(type)
        api_params['unit'] = self._normalize_value(unit)
        api_params['unit_price'] = self._normalize_value(unit_price)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=CartItem)


    def carts_items_replace(
        self,
        cart_id: str,
        items: List[CartItemCreateRequest]
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        cart_id : str
            
        items : List[CartItemCreateRequest]
            The complete new item set (set semantics).
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts/{cart_id}/items'
        api_params = {}
        if cart_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "cart_id"')

        if items is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "items"')

        api_path = api_path.replace('{cartId}', str(self._normalize_value(cart_id)))

        api_params['items'] = self._normalize_value(items)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def carts_items_delete(
        self,
        cart_id: str,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        cart_id : str
            
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

        api_path = '/v1/carts/{cart_id}/items/{id}'
        api_params = {}
        if cart_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "cart_id"')

        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{cartId}', str(self._normalize_value(cart_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def carts_items_get(
        self,
        cart_id: str,
        id: str
    ) -> CartItem:
        """
        

        Parameters
        ----------
        cart_id : str
            
        id : str
            
        
        Returns
        -------
        CartItem
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts/{cart_id}/items/{id}'
        api_params = {}
        if cart_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "cart_id"')

        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{cartId}', str(self._normalize_value(cart_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=CartItem)


    def carts_items_update(
        self,
        cart_id: str,
        id: str,
        configuration: Optional[Dict[str, Any]] = None,
        currency: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        position: Optional[float] = None,
        product_id: Optional[str] = None,
        quantity: Optional[float] = None,
        sku: Optional[str] = None,
        snapshot: Optional[Dict[str, Any]] = None,
        tax_rate: Optional[float] = None,
        type: Optional[CartItemType] = None,
        unit: Optional[str] = None,
        unit_price: Optional[float] = None
    ) -> CartItem:
        """
        

        Parameters
        ----------
        cart_id : str
            
        id : str
            
        configuration : Optional[Dict[str, Any]]
            Free-form configuration — configured lines never merge.
        currency : Optional[str]
            Defaults to the cart's currency.
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        name : Optional[str]
            Falls back to 'sku' when omitted.
        position : Optional[float]
            
        product_id : Optional[str]
            
        quantity : Optional[float]
            Default 1.
        sku : Optional[str]
            
        snapshot : Optional[Dict[str, Any]]
            Loose product snapshot at add-time (price, name, image, …).
        tax_rate : Optional[float]
            
        type : Optional[CartItemType]
            Line type (default 'product'). Plain product lines merge by product+price; configurations always stand alone.
        unit : Optional[str]
            
        unit_price : Optional[float]
            Per-unit net price — line_total is always derived.
        
        Returns
        -------
        CartItem
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts/{cart_id}/items/{id}'
        api_params = {}
        if cart_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "cart_id"')

        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{cartId}', str(self._normalize_value(cart_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['configuration'] = self._normalize_value(configuration)
        api_params['currency'] = self._normalize_value(currency)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['name'] = self._normalize_value(name)
        api_params['position'] = self._normalize_value(position)
        api_params['product_id'] = self._normalize_value(product_id)
        api_params['quantity'] = self._normalize_value(quantity)
        api_params['sku'] = self._normalize_value(sku)
        api_params['snapshot'] = self._normalize_value(snapshot)
        api_params['tax_rate'] = self._normalize_value(tax_rate)
        if type is not None:
            api_params['type'] = self._normalize_value(type)
        api_params['unit'] = self._normalize_value(unit)
        api_params['unit_price'] = self._normalize_value(unit_price)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=CartItem)


    def carts_delete(
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

        api_path = '/v1/carts/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def carts_get(
        self,
        id: str
    ) -> Cart:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Cart
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Cart)


    def carts_update(
        self,
        id: str,
        channel_id: Optional[str] = None,
        currency: Optional[str] = None,
        market_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None
    ) -> Cart:
        """
        

        Parameters
        ----------
        id : str
            
        channel_id : Optional[str]
            
        currency : Optional[str]
            ISO 4217 code.
        market_id : Optional[str]
            
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        name : Optional[str]
            
        
        Returns
        -------
        Cart
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['channel_id'] = self._normalize_value(channel_id)
        api_params['currency'] = self._normalize_value(currency)
        api_params['market_id'] = self._normalize_value(market_id)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['name'] = self._normalize_value(name)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Cart)


    def carts_abandon(
        self,
        id: str
    ) -> Cart:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Cart
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts/{id}/abandon'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=Cart)


    def carts_activate(
        self,
        id: str
    ) -> Cart:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Cart
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts/{id}/activate'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=Cart)


    def carts_export(
        self,
        id: str,
        format: Optional[CartExportFormat] = None,
        profile_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        id : str
            
        format : Optional[CartExportFormat]
            Ad-hoc export format (only without profile_id).
        profile_id : Optional[str]
            Export profile to run; ad-hoc JSON/CSV export when omitted.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts/{id}/export'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if format is not None:
            api_params['format'] = self._normalize_value(format)
        api_params['profile_id'] = self._normalize_value(profile_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def carts_order(
        self,
        id: str,
        order_ref: Optional[str] = None
    ) -> Cart:
        """
        

        Parameters
        ----------
        id : str
            
        order_ref : Optional[str]
            External order reference from order management.
        
        Returns
        -------
        Cart
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts/{id}/order'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['order_ref'] = self._normalize_value(order_ref)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Cart)


    def carts_reopen(
        self,
        id: str
    ) -> Cart:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Cart
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/carts/{id}/reopen'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=Cart)

