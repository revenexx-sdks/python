from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..enums.price_list_status import PriceListStatus;
from ..models.price_list import PriceList;
from ..enums.price_entry_type import PriceEntryType;
from ..models.price_entry import PriceEntry;
from ..models.price_entry_replace_item import PriceEntryReplaceItem;
from ..models.price_resolve_item import PriceResolveItem;

class Prices(Service):

    def __init__(self, client) -> None:
        super(Prices, self).__init__(client)

    def prices_lists_list(
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

        api_path = '/v1/prices/lists'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def prices_lists_create(
        self,
        code: str,
        name: str,
        channel_id: Optional[str] = None,
        contact_id: Optional[str] = None,
        currency: Optional[str] = None,
        description: Optional[str] = None,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        market_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        organization_id: Optional[str] = None,
        priority: Optional[float] = None,
        status: Optional[PriceListStatus] = None,
        tax_included: Optional[bool] = None,
        valid_from: Optional[str] = None,
        valid_until: Optional[str] = None
    ) -> PriceList:
        """
        

        Parameters
        ----------
        code : str
            Unique list code per tenant.
        name : str
            
        channel_id : Optional[str]
            Scope: only this channel.
        contact_id : Optional[str]
            Scope: only this contact — beats every other scope.
        currency : Optional[str]
            ISO 4217 code (default EUR) — resolution only considers lists matching the requested currency.
        description : Optional[str]
            
        is_default : Optional[bool]
            Default lists resolve last within their group.
        labels : Optional[Dict[str, Any]]
            Localised names ({de, en, …}).
        market_id : Optional[str]
            Scope: only this market.
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        organization_id : Optional[str]
            Scope: only this organization.
        priority : Optional[float]
            Tie-breaker within a specificity group (higher wins, default 0).
        status : Optional[PriceListStatus]
            Default 'active' — only active lists resolve.
        tax_included : Optional[bool]
            Gross (true) or net (false, default) prices.
        valid_from : Optional[str]
            Validity window start.
        valid_until : Optional[str]
            Validity window end.
        
        Returns
        -------
        PriceList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/prices/lists'
        api_params = {}
        if code is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "code"')

        if name is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "name"')


        api_params['channel_id'] = self._normalize_value(channel_id)
        api_params['code'] = self._normalize_value(code)
        api_params['contact_id'] = self._normalize_value(contact_id)
        if currency is not None:
            api_params['currency'] = self._normalize_value(currency)
        api_params['description'] = self._normalize_value(description)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['labels'] = self._normalize_value(labels)
        api_params['market_id'] = self._normalize_value(market_id)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['name'] = self._normalize_value(name)
        api_params['organization_id'] = self._normalize_value(organization_id)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if tax_included is not None:
            api_params['tax_included'] = self._normalize_value(tax_included)
        api_params['valid_from'] = self._normalize_value(valid_from)
        api_params['valid_until'] = self._normalize_value(valid_until)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=PriceList)


    def prices_lists_defaults(
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

        api_path = '/v1/prices/lists/defaults'
        api_params = {}

        response = self.client.call('post', api_path, {
        }, api_params)

        return response


    def prices_lists_delete(
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

        api_path = '/v1/prices/lists/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def prices_lists_get(
        self,
        id: str
    ) -> PriceList:
        """
        

        Parameters
        ----------
        id : str
            
        
        Returns
        -------
        PriceList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/prices/lists/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=PriceList)


    def prices_lists_update(
        self,
        id: str,
        channel_id: Optional[str] = None,
        code: Optional[str] = None,
        contact_id: Optional[str] = None,
        currency: Optional[str] = None,
        description: Optional[str] = None,
        is_default: Optional[bool] = None,
        labels: Optional[Dict[str, Any]] = None,
        market_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        priority: Optional[float] = None,
        status: Optional[PriceListStatus] = None,
        tax_included: Optional[bool] = None,
        valid_from: Optional[str] = None,
        valid_until: Optional[str] = None
    ) -> PriceList:
        """
        

        Parameters
        ----------
        id : str
            
        channel_id : Optional[str]
            Scope: only this channel.
        code : Optional[str]
            Unique list code per tenant.
        contact_id : Optional[str]
            Scope: only this contact — beats every other scope.
        currency : Optional[str]
            ISO 4217 code (default EUR) — resolution only considers lists matching the requested currency.
        description : Optional[str]
            
        is_default : Optional[bool]
            Default lists resolve last within their group.
        labels : Optional[Dict[str, Any]]
            Localised names ({de, en, …}).
        market_id : Optional[str]
            Scope: only this market.
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        name : Optional[str]
            
        organization_id : Optional[str]
            Scope: only this organization.
        priority : Optional[float]
            Tie-breaker within a specificity group (higher wins, default 0).
        status : Optional[PriceListStatus]
            Default 'active' — only active lists resolve.
        tax_included : Optional[bool]
            Gross (true) or net (false, default) prices.
        valid_from : Optional[str]
            Validity window start.
        valid_until : Optional[str]
            Validity window end.
        
        Returns
        -------
        PriceList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/prices/lists/{id}'
        api_params = {}
        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['channel_id'] = self._normalize_value(channel_id)
        if code is not None:
            api_params['code'] = self._normalize_value(code)
        api_params['contact_id'] = self._normalize_value(contact_id)
        if currency is not None:
            api_params['currency'] = self._normalize_value(currency)
        api_params['description'] = self._normalize_value(description)
        if is_default is not None:
            api_params['is_default'] = self._normalize_value(is_default)
        api_params['labels'] = self._normalize_value(labels)
        api_params['market_id'] = self._normalize_value(market_id)
        api_params['metadata'] = self._normalize_value(metadata)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        api_params['organization_id'] = self._normalize_value(organization_id)
        if priority is not None:
            api_params['priority'] = self._normalize_value(priority)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if tax_included is not None:
            api_params['tax_included'] = self._normalize_value(tax_included)
        api_params['valid_from'] = self._normalize_value(valid_from)
        api_params['valid_until'] = self._normalize_value(valid_until)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=PriceList)


    def prices_entries_list(
        self,
        list_id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        list_id : str
            
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/prices/lists/{list_id}/entries'
        api_params = {}
        if list_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "list_id"')

        api_path = api_path.replace('{listId}', str(self._normalize_value(list_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def prices_entries_create(
        self,
        list_id: str,
        metadata: Optional[Dict[str, Any]] = None,
        price_type: Optional[PriceEntryType] = None,
        product_id: Optional[str] = None,
        quantity_min: Optional[float] = None,
        sku: Optional[str] = None,
        unit: Optional[str] = None,
        unit_price: Optional[float] = None,
        valid_from: Optional[str] = None,
        valid_until: Optional[str] = None
    ) -> PriceEntry:
        """
        

        Parameters
        ----------
        list_id : str
            
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        price_type : Optional[PriceEntryType]
            Default 'standard'; 'on_request' is the explicit no-price marker — it stops resolution and answers "price on request".
        product_id : Optional[str]
            Priced product.
        quantity_min : Optional[float]
            Tier threshold (Staffelpreis): this price applies from this quantity (default 1).
        sku : Optional[str]
            Priced SKU (alternative to product_id).
        unit : Optional[str]
            
        unit_price : Optional[float]
            Per-unit price (default 0).
        valid_from : Optional[str]
            Per-entry validity start (promo prices).
        valid_until : Optional[str]
            Per-entry validity end.
        
        Returns
        -------
        PriceEntry
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/prices/lists/{list_id}/entries'
        api_params = {}
        if list_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "list_id"')

        api_path = api_path.replace('{listId}', str(self._normalize_value(list_id)))

        api_params['metadata'] = self._normalize_value(metadata)
        if price_type is not None:
            api_params['price_type'] = self._normalize_value(price_type)
        api_params['product_id'] = self._normalize_value(product_id)
        if quantity_min is not None:
            api_params['quantity_min'] = self._normalize_value(quantity_min)
        api_params['sku'] = self._normalize_value(sku)
        api_params['unit'] = self._normalize_value(unit)
        if unit_price is not None:
            api_params['unit_price'] = self._normalize_value(unit_price)
        api_params['valid_from'] = self._normalize_value(valid_from)
        api_params['valid_until'] = self._normalize_value(valid_until)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=PriceEntry)


    def prices_entries_replace(
        self,
        list_id: str,
        entries: List[PriceEntryReplaceItem]
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        list_id : str
            
        entries : List[PriceEntryReplaceItem]
            The complete new entry set (set semantics).
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/prices/lists/{list_id}/entries'
        api_params = {}
        if list_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "list_id"')

        if entries is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "entries"')

        api_path = api_path.replace('{listId}', str(self._normalize_value(list_id)))

        api_params['entries'] = self._normalize_value(entries)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def prices_entries_bulk(
        self,
        list_id: str,
        entries: List[PriceEntryReplaceItem]
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        list_id : str
            
        entries : List[PriceEntryReplaceItem]
            The complete new entry set (set semantics).
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/prices/lists/{list_id}/entries/bulk'
        api_params = {}
        if list_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "list_id"')

        if entries is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "entries"')

        api_path = api_path.replace('{listId}', str(self._normalize_value(list_id)))

        api_params['entries'] = self._normalize_value(entries)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def prices_entries_delete(
        self,
        list_id: str,
        id: str
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        list_id : str
            
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

        api_path = '/v1/prices/lists/{list_id}/entries/{id}'
        api_params = {}
        if list_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "list_id"')

        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{listId}', str(self._normalize_value(list_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return response


    def prices_entries_get(
        self,
        list_id: str,
        id: str
    ) -> PriceEntry:
        """
        

        Parameters
        ----------
        list_id : str
            
        id : str
            
        
        Returns
        -------
        PriceEntry
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/prices/lists/{list_id}/entries/{id}'
        api_params = {}
        if list_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "list_id"')

        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{listId}', str(self._normalize_value(list_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=PriceEntry)


    def prices_entries_update(
        self,
        list_id: str,
        id: str,
        metadata: Optional[Dict[str, Any]] = None,
        price_type: Optional[PriceEntryType] = None,
        product_id: Optional[str] = None,
        quantity_min: Optional[float] = None,
        sku: Optional[str] = None,
        unit: Optional[str] = None,
        unit_price: Optional[float] = None,
        valid_from: Optional[str] = None,
        valid_until: Optional[str] = None
    ) -> PriceEntry:
        """
        

        Parameters
        ----------
        list_id : str
            
        id : str
            
        metadata : Optional[Dict[str, Any]]
            Free-form metadata.
        price_type : Optional[PriceEntryType]
            Default 'standard'; 'on_request' is the explicit no-price marker — it stops resolution and answers "price on request".
        product_id : Optional[str]
            Priced product.
        quantity_min : Optional[float]
            Tier threshold (Staffelpreis): this price applies from this quantity (default 1).
        sku : Optional[str]
            Priced SKU (alternative to product_id).
        unit : Optional[str]
            
        unit_price : Optional[float]
            Per-unit price (default 0).
        valid_from : Optional[str]
            Per-entry validity start (promo prices).
        valid_until : Optional[str]
            Per-entry validity end.
        
        Returns
        -------
        PriceEntry
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/prices/lists/{list_id}/entries/{id}'
        api_params = {}
        if list_id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "list_id"')

        if id is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{listId}', str(self._normalize_value(list_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['metadata'] = self._normalize_value(metadata)
        if price_type is not None:
            api_params['price_type'] = self._normalize_value(price_type)
        api_params['product_id'] = self._normalize_value(product_id)
        if quantity_min is not None:
            api_params['quantity_min'] = self._normalize_value(quantity_min)
        api_params['sku'] = self._normalize_value(sku)
        api_params['unit'] = self._normalize_value(unit)
        if unit_price is not None:
            api_params['unit_price'] = self._normalize_value(unit_price)
        api_params['valid_from'] = self._normalize_value(valid_from)
        api_params['valid_until'] = self._normalize_value(valid_until)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=PriceEntry)


    def prices_resolve(
        self,
        items: List[PriceResolveItem],
        at: Optional[str] = None,
        channel_id: Optional[str] = None,
        contact_id: Optional[str] = None,
        currency: Optional[str] = None,
        market_id: Optional[str] = None,
        organization_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        

        Parameters
        ----------
        items : List[PriceResolveItem]
            Items to price (at most 200 per call).
        at : Optional[str]
            Point in time for validity windows (ISO 8601 timestamp, default now).
        channel_id : Optional[str]
            Buyer context: channel.
        contact_id : Optional[str]
            Buyer context: contact — most specific scope.
        currency : Optional[str]
            ISO 4217 code (default EUR) — only lists in this currency resolve.
        market_id : Optional[str]
            Buyer context: market.
        organization_id : Optional[str]
            Buyer context: organization.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/v1/prices/resolve'
        api_params = {}
        if items is None:
            raise RevenexxAPIRevenexxException('Missing required parameter: "items"')


        api_params['at'] = self._normalize_value(at)
        api_params['channel_id'] = self._normalize_value(channel_id)
        api_params['contact_id'] = self._normalize_value(contact_id)
        api_params['currency'] = self._normalize_value(currency)
        api_params['items'] = self._normalize_value(items)
        api_params['market_id'] = self._normalize_value(market_id)
        api_params['organization_id'] = self._normalize_value(organization_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response

