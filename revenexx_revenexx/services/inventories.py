from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.inventory_adjust_item import InventoryAdjustItem;
from ..models.inventory_availability_item import InventoryAvailabilityItem;
from ..enums.location_type import LocationType;
from ..models.location import Location;
from ..models.stock_movement import StockMovement;
from ..models.inventory_stock_item import InventoryStockItem;
from ..models.reservation import Reservation;
from ..models.stock_level import StockLevel;

class Inventories(Service):

    def __init__(self, client) -> None:
        super(Inventories, self).__init__(client)

    def inventories_adjust(
        self,
        items: List[InventoryAdjustItem],
        reason: str,
        location_code: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        items : List[InventoryAdjustItem]
            The corrections — quantities are SIGNED deltas (at most 200).
        reason : str
            Mandatory audit reason — every adjustment is a ledger row.
        location_code : Optional[str]
            Adjusted location (default 'main').
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/inventories/adjust'
        api_params = {}
        if items is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "items"')

        if reason is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "reason"')


        api_params['items'] = self._normalize_value(items)
        api_params['location_code'] = self._normalize_value(location_code)
        api_params['reason'] = self._normalize_value(reason)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def inventories_availability(
        self,
        items: List[InventoryAvailabilityItem],
        location_code: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        items : List[InventoryAvailabilityItem]
            The items to check (batch, at most 200).
        location_code : Optional[str]
            Restrict the check to one location (default: all enabled locations).
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/inventories/availability'
        api_params = {}
        if items is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "items"')


        api_params['items'] = self._normalize_value(items)
        api_params['location_code'] = self._normalize_value(location_code)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def inventories_commit(
        self,
        order_ref: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        order_ref : str
            The order whose active reservations are committed (shipment).
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/inventories/commit'
        api_params = {}
        if order_ref is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "order_ref"')


        api_params['order_ref'] = self._normalize_value(order_ref)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def inventories_locations_list(
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

        api_path = '/v1/inventories/locations'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def inventories_locations_create(
        self,
        code: str,
        name: str,
        address: Optional[Dict[str, Any]] = None,
        enabled: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        priority: Optional[float] = None,
        type: Optional[LocationType] = None
    ) -> Location:
        """
        

        Parameters
        ----------
        code : str
            Unique location code (per tenant).
        name : str
            
        address : Optional[Dict[str, Any]]
            
        enabled : Optional[bool]
            Disabled locations are skipped by availability and reserve (default true).
        labels : Optional[Dict[str, Any]]
            Localised display names ({de, en, …}).
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        priority : Optional[float]
            Sourcing order — lower wins (default 0).
        type : Optional[LocationType]
            Default 'warehouse'.
        
        Returns
        -------
        Location
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/inventories/locations'
        api_params = {}
        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')

        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')


        api_params['address'] = self._normalize_value(address)
        api_params['code'] = self._normalize_value(code)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        api_params['labels'] = self._normalize_value(labels)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['name'] = self._normalize_value(name)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if type is not None:
            api_params['type'] = self._normalize_value(type)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Location)


    def inventories_locations_defaults(
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

        api_path = '/v1/inventories/locations/defaults'
        api_params = {}

        response = self.client.call('post', api_path, {
        }, api_params)

        return response


    def inventories_locations_delete(
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

        api_path = '/v1/inventories/locations/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def inventories_locations_get(
        self,
        id: str
    ) -> Location:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Location
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/inventories/locations/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Location)


    def inventories_locations_update(
        self,
        id: str,
        address: Optional[Dict[str, Any]] = None,
        code: Optional[str] = None,
        enabled: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        priority: Optional[float] = None,
        type: Optional[LocationType] = None
    ) -> Location:
        """
        

        Parameters
        ----------
        id : str
            
        address : Optional[Dict[str, Any]]
            
        code : Optional[str]
            Unique location code (per tenant).
        enabled : Optional[bool]
            Disabled locations are skipped by availability and reserve (default true).
        labels : Optional[Dict[str, Any]]
            Localised display names ({de, en, …}).
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        name : Optional[str]
            
        priority : Optional[float]
            Sourcing order — lower wins (default 0).
        type : Optional[LocationType]
            Default 'warehouse'.
        
        Returns
        -------
        Location
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/inventories/locations/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['address'] = self._normalize_value(address)
        if code is not None:
            api_params['code'] = self._normalize_value(code)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        api_params['labels'] = self._normalize_value(labels)
        api_params['metadata'] = self._normalize_value(metadata)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if type is not None:
            api_params['type'] = self._normalize_value(type)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Location)


    def inventories_movements_list(
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

        api_path = '/v1/inventories/movements'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def inventories_movements_get(
        self,
        id: str
    ) -> StockMovement:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        StockMovement
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/inventories/movements/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=StockMovement)


    def inventories_receive(
        self,
        items: List[InventoryStockItem],
        location_code: Optional[str] = None,
        reason: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        items : List[InventoryStockItem]
            The inbound items (at most 200).
        location_code : Optional[str]
            Receiving location (default 'main').
        reason : Optional[str]
            Ledger note (e.g. delivery note number).
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/inventories/receive'
        api_params = {}
        if items is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "items"')


        api_params['items'] = self._normalize_value(items)
        api_params['location_code'] = self._normalize_value(location_code)
        api_params['reason'] = self._normalize_value(reason)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def inventories_release(
        self,
        order_ref: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        order_ref : str
            The order whose active reservations are released.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/inventories/release'
        api_params = {}
        if order_ref is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "order_ref"')


        api_params['order_ref'] = self._normalize_value(order_ref)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def inventories_reservations_list(
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

        api_path = '/v1/inventories/reservations'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def inventories_reservations_get(
        self,
        id: str
    ) -> Reservation:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        Reservation
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/inventories/reservations/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Reservation)


    def inventories_reserve(
        self,
        items: List[InventoryStockItem],
        order_ref: str,
        expires_at: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        items : List[InventoryStockItem]
            The items to reserve — all-or-nothing (at most 200).
        order_ref : str
            The order this reservation belongs to.
        expires_at : Optional[str]
            Optional reservation expiry.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/inventories/reserve'
        api_params = {}
        if items is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "items"')

        if order_ref is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "order_ref"')


        api_params['expires_at'] = self._normalize_value(expires_at)
        api_params['items'] = self._normalize_value(items)
        api_params['order_ref'] = self._normalize_value(order_ref)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def inventories_restock(
        self,
        items: List[InventoryStockItem],
        location_code: Optional[str] = None,
        order_ref: Optional[str] = None,
        reason: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        items : List[InventoryStockItem]
            The returned items (at most 200).
        location_code : Optional[str]
            Restocking location (default 'main').
        order_ref : Optional[str]
            Originating order (ledger reference).
        reason : Optional[str]
            Ledger note (e.g. return reason).
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/inventories/restock'
        api_params = {}
        if items is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "items"')


        api_params['items'] = self._normalize_value(items)
        api_params['location_code'] = self._normalize_value(location_code)
        api_params['order_ref'] = self._normalize_value(order_ref)
        api_params['reason'] = self._normalize_value(reason)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def inventories_stock_list(
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

        api_path = '/v1/inventories/stock'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def inventories_stock_create(
        self,
        location_id: str,
        metadata: Optional[Dict[str, Any]] = None,
        on_hand: Optional[float] = None,
        product_id: Optional[str] = None,
        reorder_point: Optional[float] = None,
        reserved: Optional[float] = None,
        sku: Optional[str] = None
    ) -> StockLevel:
        """
        

        Parameters
        ----------
        location_id : str
            Owning location.
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        on_hand : Optional[float]
            Physical stock (default 0).
        product_id : Optional[str]
            Tracked product.
        reorder_point : Optional[float]
            
        reserved : Optional[float]
            Reserved stock (default 0) — normally managed by reserve/release/commit.
        sku : Optional[str]
            Tracked SKU (alternative to product_id).
        
        Returns
        -------
        StockLevel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/inventories/stock'
        api_params = {}
        if location_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "location_id"')


        api_params['location_id'] = self._normalize_value(location_id)
        api_params['metadata'] = self._normalize_value(metadata)
        if on_hand is not None:
            api_params['on_hand'] = self._normalize_value(on_hand)
        api_params['product_id'] = self._normalize_value(product_id)
        api_params['reorder_point'] = self._normalize_value(reorder_point)
        if reserved is not None:
            api_params['reserved'] = self._normalize_value(reserved)
        api_params['sku'] = self._normalize_value(sku)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=StockLevel)


    def inventories_stock_delete(
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

        api_path = '/v1/inventories/stock/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def inventories_stock_get(
        self,
        id: str
    ) -> StockLevel:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        StockLevel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/inventories/stock/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=StockLevel)


    def inventories_stock_update(
        self,
        id: str,
        location_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        on_hand: Optional[float] = None,
        product_id: Optional[str] = None,
        reorder_point: Optional[float] = None,
        reserved: Optional[float] = None,
        sku: Optional[str] = None
    ) -> StockLevel:
        """
        

        Parameters
        ----------
        id : str
            
        location_id : Optional[str]
            Owning location.
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        on_hand : Optional[float]
            Physical stock (default 0).
        product_id : Optional[str]
            Tracked product.
        reorder_point : Optional[float]
            
        reserved : Optional[float]
            Reserved stock (default 0) — normally managed by reserve/release/commit.
        sku : Optional[str]
            Tracked SKU (alternative to product_id).
        
        Returns
        -------
        StockLevel
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/inventories/stock/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if location_id is not None:
            api_params['location_id'] = self._normalize_value(location_id)
        api_params['metadata'] = self._normalize_value(metadata)
        if on_hand is not None:
            api_params['on_hand'] = self._normalize_value(on_hand)
        api_params['product_id'] = self._normalize_value(product_id)
        api_params['reorder_point'] = self._normalize_value(reorder_point)
        if reserved is not None:
            api_params['reserved'] = self._normalize_value(reserved)
        api_params['sku'] = self._normalize_value(sku)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=StockLevel)

