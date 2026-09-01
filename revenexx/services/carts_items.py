from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..enums.cart_item_type import CartItemType;
from ..models.error import Error;
from ..models.cart_item_create_request import CartItemCreateRequest;

class CartsItems(Service):

    def __init__(self, client) -> None:
        super(CartsItems, self).__init__(client)

    def carts_items_list(
        self,
        cart_id: str,
        id: Optional[str] = None,
        type: Optional[CartItemType] = None,
        product_id: Optional[str] = None,
        sku: Optional[str] = None,
        name: Optional[str] = None,
        quantity: Optional[float] = None,
        unit: Optional[str] = None,
        unit_price: Optional[float] = None,
        currency: Optional[str] = None,
        tax_rate: Optional[float] = None,
        line_total: Optional[float] = None,
        position: Optional[float] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Error:
        """
        The array is still called 'items'; the response also carries 'page' and 'filter' like every other list, and an unknown cart_id answers 404 instead of an empty page. A cart with more lines than the page size is not silently truncated — 'page.hasMore' says so. Lines come back in position order unless 'order' says otherwise.

        Parameters
        ----------
        cart_id : str
            The cart the line belongs to, by its id. An id no cart in this tenant has answers 404 rather than an empty list, so a wrong cart is never mistaken for an empty one.
        id : Optional[str]
            One line, in list form.
        type : Optional[CartItemType]
            Product lines, configured lines or custom lines.
        product_id : Optional[str]
            Lines for one catalogue product.
        sku : Optional[str]
            Exact article number — the join every ERP integration makes. Not a search: no prefix, no wildcard.
        name : Optional[str]
            Exact line name. Not a search.
        quantity : Optional[float]
            Exact quantity — equality, so it matches a line of exactly this many, never 'at least'.
        unit : Optional[str]
            Lines counted in one unit ('pcs', 'm').
        unit_price : Optional[float]
            Exact unit price — the lines still sitting at one particular number after a repricing run.
        currency : Optional[str]
            Lines priced in one currency — normally the cart's, so this earns its place only where a cart mixes them.
        tax_rate : Optional[float]
            Lines at one VAT rate.
        line_total : Optional[float]
            Exact line total. Equality only — there is no range form, so this finds `0` and little else.
        position : Optional[float]
            The line at one position.
        created_at : Optional[str]
            Exact instant, not a range.
        updated_at : Optional[str]
            Exact instant, not a range.
        limit : Optional[float]
            Page size (default 50, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. Anything else is refused with 400.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts/{cart_id}/items'
        api_params = {}
        if cart_id is None:
            raise RevenexxException('Missing required parameter: "cart_id"')

        api_path = api_path.replace('{cart_id}', str(self._normalize_value(cart_id)))

        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if type is not None:
            api_params['type'] = self._normalize_value(type)
        if product_id is not None:
            api_params['product_id'] = self._normalize_value(product_id)
        if sku is not None:
            api_params['sku'] = self._normalize_value(sku)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if quantity is not None:
            api_params['quantity'] = self._normalize_value(quantity)
        if unit is not None:
            api_params['unit'] = self._normalize_value(unit)
        if unit_price is not None:
            api_params['unit_price'] = self._normalize_value(unit_price)
        if currency is not None:
            api_params['currency'] = self._normalize_value(currency)
        if tax_rate is not None:
            api_params['tax_rate'] = self._normalize_value(tax_rate)
        if line_total is not None:
            api_params['line_total'] = self._normalize_value(line_total)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if created_at is not None:
            api_params['created_at'] = self._normalize_value(created_at)
        if updated_at is not None:
            api_params['updated_at'] = self._normalize_value(updated_at)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


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
    ) -> Error:
        """
        Adds one line to an ACTIVE cart — the add-to-basket call. `name` or `sku` is required (a line sent with only a SKU takes the SKU as its name, so a line always has something to show) and `quantity` must be greater than zero; everything else defaults, including the currency, which falls back to the cart's. The one thing that surprises a caller: a plain product line with the same product/sku AND the same `unit_price` as a line already in the cart does not open a second row — its quantity is added to that line, and the 201 names a row that already existed. Price is part of that identity on purpose, so a changed price never averages into an old line. A configured or custom line always stands alone. The cart's `item_count` (the sum of QUANTITIES) and `subtotal` are recomputed before the answer, and `max_items_per_cart` / `max_quantity_per_line` are checked on the RESULT of the merge (422), so ten calls of one piece cannot walk past a limit one call of ten would hit.

        Parameters
        ----------
        cart_id : str
            The cart the line belongs to, by its id. An id no cart in this tenant has answers 404 rather than an empty list, so a wrong cart is never mistaken for an empty one.
        configuration : Optional[Dict[str, Any]]
            What was configured on this line, in the configurator's own vocabulary — this app stores it and reads nothing out of it. Its mere PRESENCE is behaviour: a line that carries a configuration never merges with another, because two differently configured units of the same article are not one line. Keys are the configurator's; the example is one shape, not the shape.
        currency : Optional[str]
            ISO 4217 code. Defaults to the cart's currency.
        metadata : Optional[Dict[str, Any]]
            Free-form data the storefront hangs on the line. Stored and returned verbatim; no key in here is read by this app.
        name : Optional[str]
            What the line reads as on the cart page. Falls back to 'sku' when omitted, so a line always has something to show.
        position : Optional[float]
            Sort order within the cart, ascending. Default 0 when adding a line; in a bulk replace the payload order fills it in.
        product_id : Optional[str]
            The catalogue product, when the line comes from one. Part of the merge identity: same product, same price, one line.
        quantity : Optional[float]
            How much of it — default 1. Fractional is legal (2.5 m of cable); zero and negative are not. On a plain product line that merges into an existing one, this is ADDED to what is already there, and max_quantity_per_line is checked on the result.
        sku : Optional[str]
            The article number, exactly as the merchant knows it. Free text — this app does not resolve it against the catalogue — and part of the merge identity together with product_id and unit_price. The example only shows the shape of a real article number; nothing here enforces one.
        snapshot : Optional[Dict[str, Any]]
            The product as the buyer was shown it when this line was added — the cart's own copy, so it stays honest when the catalogue moves underneath it. Free-form apart from the price: conversion reads `unit_price` (or `price` as a fallback) and nothing else. A snapshot without a readable price leaves the line alone in both price modes, which is deliberate — a missing snapshot must never be read as "free".
        tax_rate : Optional[float]
            VAT percent for this line, as a number (19 means 19 %). Stored for the order to use — no total in this app includes tax.
        type : Optional[CartItemType]
            Line type (default 'product'). Plain product lines merge by product+price; configurations always stand alone.
        unit : Optional[str]
            The unit the quantity is counted in. Display and ERP hand-over only — this app converts nothing.
        unit_price : Optional[float]
            Net price of one unit — line_total is always derived from it, never sent. Part of the merge identity: the same article at a different price opens a new line rather than averaging into the old one.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts/{cart_id}/items'
        api_params = {}
        if cart_id is None:
            raise RevenexxException('Missing required parameter: "cart_id"')

        api_path = api_path.replace('{cart_id}', str(self._normalize_value(cart_id)))

        api_params['configuration'] = self._normalize_value(configuration)
        api_params['currency'] = self._normalize_value(currency)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['name'] = self._normalize_value(name)
        api_params['position'] = self._normalize_value(position)
        api_params['product_id'] = self._normalize_value(product_id)
        api_params['quantity'] = self._normalize_value(quantity)
        api_params['sku'] = self._normalize_value(sku)
        if snapshot is not None:
            api_params['snapshot'] = self._normalize_value(snapshot)
        api_params['tax_rate'] = self._normalize_value(tax_rate)
        if type is not None:
            api_params['type'] = self._normalize_value(type)
        api_params['unit'] = self._normalize_value(unit)
        api_params['unit_price'] = self._normalize_value(unit_price)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def carts_items_replace(
        self,
        cart_id: str,
        items: List[CartItemCreateRequest]
    ) -> Error:
        """
        Set semantics: the payload IS the cart. Every existing line is dropped and the payload is written in its place, so a line left out of the array is a line removed — this is the storefront sync, not a bulk add, and carts.items.create is what adds. Lines are numbered by their place in the array unless they carry their own `position`, and nothing merges: two identical lines in one payload stay two rows. The limits are checked against the payload BEFORE a single existing line is destroyed, so a sync refused with 422 leaves the cart exactly as it was. The cart must be active, and its totals are recomputed before the answer.

        Parameters
        ----------
        cart_id : str
            The cart the line belongs to, by its id. An id no cart in this tenant has answers 404 rather than an empty list, so a wrong cart is never mistaken for an empty one.
        items : List[CartItemCreateRequest]
            The complete new item set (set semantics).
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts/{cart_id}/items'
        api_params = {}
        if cart_id is None:
            raise RevenexxException('Missing required parameter: "cart_id"')

        if items is None:
            raise RevenexxException('Missing required parameter: "items"')

        api_path = api_path.replace('{cart_id}', str(self._normalize_value(cart_id)))

        api_params['items'] = self._normalize_value(items)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def carts_items_delete(
        self,
        cart_id: str,
        id: str
    ) -> Error:
        """
        Removes one line from an ACTIVE cart and recomputes the owning cart's `item_count` and `subtotal` before answering. This is how a quantity reaches zero: `quantity` is constrained to be greater than zero, so "none of it" is a DELETE and never an update to 0. The cart in the path is part of the address — a line belonging to a different cart answers 404 and is left where it is. Deleting the last line leaves an empty cart, not a deleted one; the cart itself goes through carts.delete, which takes every line with it in one call.

        Parameters
        ----------
        cart_id : str
            The cart the line belongs to, by its id. An id no cart in this tenant has answers 404 rather than an empty list, so a wrong cart is never mistaken for an empty one.
        id : str
            The line, by its id. The cart in the path is checked too: a line that belongs to a different cart answers 404, so an id guessed from another cart never resolves here.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts/{cart_id}/items/{id}'
        api_params = {}
        if cart_id is None:
            raise RevenexxException('Missing required parameter: "cart_id"')

        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{cart_id}', str(self._normalize_value(cart_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def carts_items_get(
        self,
        cart_id: str,
        id: str
    ) -> Error:
        """
        One line, addressed through the cart that owns it. Both ids are checked, not just the line's: a line that exists but belongs to a different cart answers 404 rather than the row, so an id copied out of another cart never resolves here and a caller can trust that what came back is a line of the cart they asked about. The line carries both of its prices — the working `unit_price`, which a resync or a repricing job may have moved, and the `snapshot` the buyer was shown when the line was added — and its own `line_total`, which is always quantity × unit_price and never what a payload claimed. To read a whole cart's lines, list them: this route is for one known line.

        Parameters
        ----------
        cart_id : str
            The cart the line belongs to, by its id. An id no cart in this tenant has answers 404 rather than an empty list, so a wrong cart is never mistaken for an empty one.
        id : str
            The line, by its id. The cart in the path is checked too: a line that belongs to a different cart answers 404, so an id guessed from another cart never resolves here.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts/{cart_id}/items/{id}'
        api_params = {}
        if cart_id is None:
            raise RevenexxException('Missing required parameter: "cart_id"')

        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{cart_id}', str(self._normalize_value(cart_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


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
    ) -> Error:
        """
        Changes one line of an ACTIVE cart — the quantity stepper on the cart page, and the route a repricing job writes through. The fields sent are merged onto the stored line and the whole line is validated again, so `quantity` must still be greater than zero and `type` still one of the three. `line_total` is not settable: it is recomputed as quantity × unit_price, and the cart's `item_count` and `subtotal` follow before the answer. What it will NOT do is merge — only carts.items.create folds one line into another, so giving this line the same product and price as a sibling leaves two rows standing, and the next add joins whichever it matches. `max_quantity_per_line` is enforced on the result (422). A quantity of zero is not the way to remove a line; the delete is.

        Parameters
        ----------
        cart_id : str
            The cart the line belongs to, by its id. An id no cart in this tenant has answers 404 rather than an empty list, so a wrong cart is never mistaken for an empty one.
        id : str
            The line, by its id. The cart in the path is checked too: a line that belongs to a different cart answers 404, so an id guessed from another cart never resolves here.
        configuration : Optional[Dict[str, Any]]
            What was configured on this line, in the configurator's own vocabulary — this app stores it and reads nothing out of it. Its mere PRESENCE is behaviour: a line that carries a configuration never merges with another, because two differently configured units of the same article are not one line. Keys are the configurator's; the example is one shape, not the shape.
        currency : Optional[str]
            ISO 4217 code. Defaults to the cart's currency.
        metadata : Optional[Dict[str, Any]]
            Free-form data the storefront hangs on the line. Stored and returned verbatim; no key in here is read by this app.
        name : Optional[str]
            What the line reads as on the cart page. Falls back to 'sku' when omitted, so a line always has something to show.
        position : Optional[float]
            Sort order within the cart, ascending. Default 0 when adding a line; in a bulk replace the payload order fills it in.
        product_id : Optional[str]
            The catalogue product, when the line comes from one. Part of the merge identity: same product, same price, one line.
        quantity : Optional[float]
            How much of it — default 1. Fractional is legal (2.5 m of cable); zero and negative are not. On a plain product line that merges into an existing one, this is ADDED to what is already there, and max_quantity_per_line is checked on the result.
        sku : Optional[str]
            The article number, exactly as the merchant knows it. Free text — this app does not resolve it against the catalogue — and part of the merge identity together with product_id and unit_price. The example only shows the shape of a real article number; nothing here enforces one.
        snapshot : Optional[Dict[str, Any]]
            The product as the buyer was shown it when this line was added — the cart's own copy, so it stays honest when the catalogue moves underneath it. Free-form apart from the price: conversion reads `unit_price` (or `price` as a fallback) and nothing else. A snapshot without a readable price leaves the line alone in both price modes, which is deliberate — a missing snapshot must never be read as "free".
        tax_rate : Optional[float]
            VAT percent for this line, as a number (19 means 19 %). Stored for the order to use — no total in this app includes tax.
        type : Optional[CartItemType]
            Line type (default 'product'). Plain product lines merge by product+price; configurations always stand alone.
        unit : Optional[str]
            The unit the quantity is counted in. Display and ERP hand-over only — this app converts nothing.
        unit_price : Optional[float]
            Net price of one unit — line_total is always derived from it, never sent. Part of the merge identity: the same article at a different price opens a new line rather than averaging into the old one.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/carts/{cart_id}/items/{id}'
        api_params = {}
        if cart_id is None:
            raise RevenexxException('Missing required parameter: "cart_id"')

        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{cart_id}', str(self._normalize_value(cart_id)))
        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['configuration'] = self._normalize_value(configuration)
        api_params['currency'] = self._normalize_value(currency)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['name'] = self._normalize_value(name)
        api_params['position'] = self._normalize_value(position)
        api_params['product_id'] = self._normalize_value(product_id)
        api_params['quantity'] = self._normalize_value(quantity)
        api_params['sku'] = self._normalize_value(sku)
        if snapshot is not None:
            api_params['snapshot'] = self._normalize_value(snapshot)
        api_params['tax_rate'] = self._normalize_value(tax_rate)
        if type is not None:
            api_params['type'] = self._normalize_value(type)
        api_params['unit'] = self._normalize_value(unit)
        api_params['unit_price'] = self._normalize_value(unit_price)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)

