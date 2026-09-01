from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..models.inventory_adjust_item import InventoryAdjustItem;
from ..models.error import Error;
from ..models.inventory_availability_item import InventoryAvailabilityItem;
from ..enums.inventories_movements_list_type import InventoriesMovementsListType;
from ..models.inventory_stock_item import InventoryStockItem;
from ..models.reorder_alerts import ReorderAlerts;
from ..models.reorder_scan import ReorderScan;
from ..models.inventory_vocabulary_index import InventoryVocabularyIndex;
from ..enums.inventories_vocabularies_get_name import InventoriesVocabulariesGetName;

class InventoriesStock(Service):

    def __init__(self, client) -> None:
        super(InventoriesStock, self).__init__(client)

    def inventories_adjust(
        self,
        items: Optional[List[InventoryAdjustItem]] = None,
        location_code: Optional[str] = None,
        product_id: Optional[str] = None,
        quantity: Optional[float] = None,
        reason: Optional[str] = None,
        sku: Optional[str] = None
    ) -> Error:
        """
        The batch correction route — a stocktake, breakage, shrinkage — and the manual way `on_hand` is ever put right. Quantities are SIGNED: a positive one adds to the balance, a negative one takes it away, and neither is written onto the row directly. Each item is booked into the movements ledger as an `adjustment` and the balance follows, so a correction leaves a record of who changed what and why instead of a number that silently differs from yesterday's. A reason is mandatory unless movement_reason_required is 'none'.

        Parameters
        ----------
        items : Optional[List[InventoryAdjustItem]]
            The corrections, at most 200 in one call — a stocktake, breakage, shrinkage. Quantities are SIGNED deltas, not new balances.
        location_code : Optional[str]
            Which location is being corrected. Omitted, the `default_location_code` setting decides. A correction is per location: the same SKU in two warehouses is two corrections.
        product_id : Optional[str]
            Inline single-item form: the product to move, instead of a one-entry `items` array. The two forms are equivalent — nothing downstream knows which arrived.
        quantity : Optional[float]
            Inline single-item form: the SIGNED correction (negative writes stock off, positive finds it). Non-zero.
        reason : Optional[str]
            Why the stock is being corrected — this is the audit trail a stocktake leaves behind. Owed unless `movement_reason_required` is 'none' (its default, 'adjustments', asks for one exactly here); missing where it is owed, the call is 400.
        sku : Optional[str]
            Inline single-item form: the article number to move (instead of `product_id`).
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/adjust'
        api_params = {}

        if items is not None:
            api_params['items'] = self._normalize_value(items)
        api_params['location_code'] = self._normalize_value(location_code)
        api_params['product_id'] = self._normalize_value(product_id)
        api_params['quantity'] = self._normalize_value(quantity)
        api_params['reason'] = self._normalize_value(reason)
        api_params['sku'] = self._normalize_value(sku)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def inventories_availability(
        self,
        items: Optional[List[InventoryAvailabilityItem]] = None,
        location_code: Optional[str] = None,
        product_id: Optional[str] = None,
        quantity: Optional[float] = None,
        sku: Optional[str] = None
    ) -> Error:
        """
        THE stock call of this app, and a batch one: name any number of items and each comes back with `on_hand`, `reserved` and the derived `available` (their difference, computed on read and stored nowhere), summed across the locations in scope and broken down per location, plus `orderable` — whether this much of it can be promised at this moment. An item this app has never seen is NOT an error: it comes back tracked:false, and the storefront decides whether an untracked item sells freely. It is also the most customised surface this product has in the field. A tenant whose stock really lives in an ERP — SAP live stock is the ordinary case, not the exotic one — replaces exactly this one capability, 1:1, with a custom app through the gateway's capability override, while every other route here keeps doing the stock-keeping CRUD unchanged. That is why the request and response shapes below read as a contract to be implemented rather than as an implementation detail: whatever ends up answering this path has to answer in these terms.

        Parameters
        ----------
        items : Optional[List[InventoryAvailabilityItem]]
            The items to check, at most 200 in one call. A cart, a category page, a feed row — one call answers them all, which is why this route is the batch one.
        location_code : Optional[str]
            Restrict the check to ONE location, by its code — the stock a click-and-collect store can promise today. Omitted, every ENABLED location is summed; a disabled one is never counted either way.
        product_id : Optional[str]
            Inline single-item form: the product to move, instead of a one-entry `items` array. The two forms are equivalent — nothing downstream knows which arrived.
        quantity : Optional[float]
            Inline single-item form: how many are wanted (default 1). It decides `orderable` and nothing else.
        sku : Optional[str]
            Inline single-item form: the article number to move (instead of `product_id`).
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/availability'
        api_params = {}

        if items is not None:
            api_params['items'] = self._normalize_value(items)
        api_params['location_code'] = self._normalize_value(location_code)
        api_params['product_id'] = self._normalize_value(product_id)
        api_params['quantity'] = self._normalize_value(quantity)
        api_params['sku'] = self._normalize_value(sku)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def inventories_movements_list(
        self,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None,
        id: Optional[str] = None,
        location_id: Optional[str] = None,
        product_id: Optional[str] = None,
        sku: Optional[str] = None,
        type: Optional[InventoriesMovementsListType] = None,
        quantity: Optional[float] = None,
        order_ref: Optional[str] = None,
        reason: Optional[str] = None,
        metadata: Optional[str] = None,
        created_at: Optional[str] = None
    ) -> Error:
        """
        The movements ledger, read end to end. Every stock change this app has ever made is a booking row in it — a receipt, a correction, a hold, a release, a shipment, a return — which is what lets one list be an audit trail and an event feed at the same time: these are the rows the `stock_movement.created` event carries, so a consumer that missed an event catches up by paging here. Append-only: the ledger has no update and no delete, because a correction is another booking. `order=created_at.desc` is the feed order.

        Parameters
        ----------
        limit : Optional[float]
            Page size (default 50, max 200). A larger value is clamped rather than refused.
        offset : Optional[float]
            Row offset for pagination (default 0). Page with `page.total` and `page.hasMore`.
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc' — a bare column sorts ascending. The column has to be one this entity has; anything else is refused with 400.
        id : Optional[str]
            Exact-match filter on `id`. The row's own id, generated by the database.
        location_id : Optional[str]
            Exact-match filter on `location_id`. Every booking at one location.
        product_id : Optional[str]
            Exact-match filter on `product_id`. The product this booking is for, copied from the call.
        sku : Optional[str]
            Exact-match filter on `sku`. Every booking for one SKU.
        type : Optional[InventoriesMovementsListType]
            Exact-match filter on `type`. What the booking records. The permitted set is the CHECK constraint — GET /inventories/vocabularies/movement-types has the words for it.
        quantity : Optional[float]
            Exact-match filter on `quantity`. Exact signed quantity, which is a needle-in-a-haystack filter rather than a range: `?quantity=-5` finds the bookings that moved exactly five out.
        order_ref : Optional[str]
            Exact-match filter on `order_ref`. One order's whole stock history: its reserve, release, shipment and restock bookings.
        reason : Optional[str]
            Exact-match filter on `reason`. Why the booking happened, in a person's words — a delivery note number, 'stocktake 2026-03', 'damaged in transit'.
        metadata : Optional[str]
            Exact-match filter on `metadata`. Free-form, and two keys this app writes itself: `backordered` — on a `reserve` booking, how much of the hold was not covered by stock on hand; `shortfall` — on a `shipment` booking, how much was committed that was not physically there (`on_hand` floors at 0, so the difference is recorded here instead of vanishing). The WHOLE jsonb document is compared, serialized as JSON — this is equality, not a key lookup or a containment query, and a value that does not parse is answered 400.
        created_at : Optional[str]
            Exact-match filter on `created_at`. Exact timestamp. There is no range filter on the ledger — page it with `?order=created_at.desc` instead.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/movements'
        api_params = {}

        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)
        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if location_id is not None:
            api_params['location_id'] = self._normalize_value(location_id)
        if product_id is not None:
            api_params['product_id'] = self._normalize_value(product_id)
        if sku is not None:
            api_params['sku'] = self._normalize_value(sku)
        if type is not None:
            api_params['type'] = self._normalize_value(type)
        if quantity is not None:
            api_params['quantity'] = self._normalize_value(quantity)
        if order_ref is not None:
            api_params['order_ref'] = self._normalize_value(order_ref)
        if reason is not None:
            api_params['reason'] = self._normalize_value(reason)
        if metadata is not None:
            api_params['metadata'] = self._normalize_value(metadata)
        if created_at is not None:
            api_params['created_at'] = self._normalize_value(created_at)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def inventories_movements_get(
        self,
        id: str
    ) -> Error:
        """
        A movement is one booking row in the ledger, and the ledger is append-only: there is no update and no delete, because a correction is another booking. `quantity` is SIGNED and its sign follows the `type` — a receipt books +5 and the reserve that promises those goods books −5, even though the reservation it created carries +5 as a positive hold. GET /inventories/vocabularies/movement-types is the list of types with the words for them. A booking says what changed, not what the balance became: it carries no running total, so the row's story is read by listing the ledger for that location and item rather than by fetching one id. `location_id` is a plain uuid and not a foreign key, so a booking outlives the location it was made at and this route will happily hand back one whose location no longer resolves — that is the audit trail doing its job, not a broken row. Fixing a wrong booking is another booking (POST /inventories/adjust); nothing here can be edited or removed.

        Parameters
        ----------
        id : str
            The ledger booking.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/movements/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def inventories_receive(
        self,
        items: Optional[List[InventoryStockItem]] = None,
        location_code: Optional[str] = None,
        product_id: Optional[str] = None,
        quantity: Optional[float] = None,
        reason: Optional[str] = None,
        sku: Optional[str] = None
    ) -> Error:
        """
        Books a delivery into the receiving location (the caller's location_code, else the default_location_code setting), creating the stock row if the item is new. A reason is optional unless movement_reason_required is 'all'. Takes a batch or one item inline.

        Parameters
        ----------
        items : Optional[List[InventoryStockItem]]
            The goods that arrived, at most 200 in one call — a delivery, a production batch, an opening balance.
        location_code : Optional[str]
            Which location took the delivery. Omitted, the `default_location_code` setting decides; a code no location carries is answered 400 rather than booked somewhere else.
        product_id : Optional[str]
            Inline single-item form: the product to move, instead of a one-entry `items` array. The two forms are equivalent — nothing downstream knows which arrived.
        quantity : Optional[float]
            Inline single-item form: how many arrived. Positive.
        reason : Optional[str]
            What the ledger should record about this receipt — a delivery note number, a production order. Owed only when `movement_reason_required` is 'all'; the contract does not require it, because whether it is owed is the tenant's setting and not this route's rule.
        sku : Optional[str]
            Inline single-item form: the article number to move (instead of `product_id`).
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/receive'
        api_params = {}

        if items is not None:
            api_params['items'] = self._normalize_value(items)
        api_params['location_code'] = self._normalize_value(location_code)
        api_params['product_id'] = self._normalize_value(product_id)
        api_params['quantity'] = self._normalize_value(quantity)
        api_params['reason'] = self._normalize_value(reason)
        api_params['sku'] = self._normalize_value(sku)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def inventories_reorder_alerts(
        self
    ) -> ReorderAlerts:
        """
        The replenishment worklist: the stock rows that have run down far enough that somebody has to order more, in one list rather than as a query a caller has to build. Computed on read, so it is never stale: a row alerts when available (on_hand − reserved) has fallen to or below its own reorder_point, or the reorder_point_default setting when it carries none. A point of 0 never alerts. Answers enabled:false with an empty list when reorder_alert_enabled is off — a tenant replenishing from an ERP should not be told twice.

        Returns
        -------
        ReorderAlerts
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/reorder-alerts'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ReorderAlerts)


    def inventories_reorder_scan(
        self,
        data: Dict[str, Any]
    ) -> ReorderScan:
        """
        Publishes `stock_level.low` on the event bus for every row GET /inventories/reorder-alerts currently lists, so replenishment can be driven by a subscriber instead of by somebody refreshing that page. Also runs hourly as the `reorder-scan` schedule; this route is for driving it on demand. The event id is derived from the stock row and the day, so a re-run — a second click, a retried cron tick — publishes nothing new and returns the ids the first run produced. Nothing is written to the app's own data: this reads the same figures the alerts list computes and hands them to the bus. Answers enabled:false without publishing when reorder_alert_enabled is off.

        Parameters
        ----------
        data : Dict[str, Any]
            Request body
        
        Returns
        -------
        ReorderScan
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/reorder-alerts/scan'
        api_params = {}
        if data is None:
            raise RevenexxException('Missing required parameter: "data"')


        api_params['data'] = self._normalize_value(data)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ReorderScan)


    def inventories_restock(
        self,
        items: Optional[List[InventoryStockItem]] = None,
        location_code: Optional[str] = None,
        order_ref: Optional[str] = None,
        product_id: Optional[str] = None,
        quantity: Optional[float] = None,
        reason: Optional[str] = None,
        restock: Optional[bool] = None,
        sku: Optional[str] = None
    ) -> Error:
        """
        Whether a return rejoins sellable stock follows restock_on_return_default, overridable per call with 'restock'. When the answer is no the response says restocked:false and nothing moves — there is no movement to book, because no stock moved. That branch is why this route answers 200 and its sibling `receive` answers 201: a restock may legitimately create nothing.

        Parameters
        ----------
        items : Optional[List[InventoryStockItem]]
            The goods that came back, at most 200 in one call. Whether they rejoin sellable stock is `restock`, not this list.
        location_code : Optional[str]
            Where the goods came back to — a returns warehouse is a location like any other. Omitted, the `default_location_code` setting decides.
        order_ref : Optional[str]
            The order the goods came back from. It is written onto the ledger booking, so the return shows up in that order's stock history next to its reserve and shipment — no reservation is touched by it.
        product_id : Optional[str]
            Inline single-item form: the product to move, instead of a one-entry `items` array. The two forms are equivalent — nothing downstream knows which arrived.
        quantity : Optional[float]
            Inline single-item form: how many came back. Positive.
        reason : Optional[str]
            Why the goods came back — 'wrong size', 'damaged on arrival'. Owed only when `movement_reason_required` is 'all'.
        restock : Optional[bool]
            Do these goods rejoin SELLABLE stock? A merchant decision, not a fact: apparel usually restocks, hygiene articles never do, many merchants inspect first. Omit it to follow the `restock_on_return_default` setting. `false` answers `restocked: false`, moves nothing and books NOTHING — there is no movement to write, because no stock moved, and that is the branch that makes this route a 200 while its sibling `receive` is a 201.
        sku : Optional[str]
            Inline single-item form: the article number to move (instead of `product_id`).
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/restock'
        api_params = {}

        if items is not None:
            api_params['items'] = self._normalize_value(items)
        api_params['location_code'] = self._normalize_value(location_code)
        api_params['order_ref'] = self._normalize_value(order_ref)
        api_params['product_id'] = self._normalize_value(product_id)
        api_params['quantity'] = self._normalize_value(quantity)
        api_params['reason'] = self._normalize_value(reason)
        api_params['restock'] = self._normalize_value(restock)
        api_params['sku'] = self._normalize_value(sku)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def inventories_stock_list(
        self,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None,
        id: Optional[str] = None,
        location_id: Optional[str] = None,
        product_id: Optional[str] = None,
        sku: Optional[str] = None,
        on_hand: Optional[float] = None,
        reserved: Optional[float] = None,
        reorder_point: Optional[float] = None,
        metadata: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None
    ) -> Error:
        """
        A stock level is ONE item at ONE location, and it carries two numbers, neither of which is the sellable one: `on_hand` is what is physically there INCLUDING everything already promised, and `reserved` is what has been promised — it never reduces `on_hand`. What may still be sold is their difference, and it is derived on read and never stored, so there is no `available` column to read, filter or order by. This is the operator's view — the whole book, filtered by location or by item — not the shop's: a storefront asking "can I sell five of this" wants POST /inventories/availability, which sums an item across locations and answers `orderable` instead of leaving the caller to subtract. Two things this list will not do: it has no range filters, so "everything running low" is GET /inventories/reorder-alerts and not a query here; and it does not promise one row per item per location — no unique index enforces that. POST /inventories/stock refuses a duplicate with a 409, but that is a check and not a constraint, so a row written past it, or one that predates the guard, still splits an item's balance in two, and the write routes find and update whichever of them the database returns first.

        Parameters
        ----------
        limit : Optional[float]
            Page size (default 50, max 200). A larger value is clamped rather than refused.
        offset : Optional[float]
            Row offset for pagination (default 0). Page with `page.total` and `page.hasMore`.
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc' — a bare column sorts ascending. The column has to be one this entity has; anything else is refused with 400.
        id : Optional[str]
            Exact-match filter on `id`. The row's own id, generated by the database.
        location_id : Optional[str]
            Exact-match filter on `location_id`. The rows held at one location. An id no location carries is an empty page, not an error.
        product_id : Optional[str]
            Exact-match filter on `product_id`. The rows tracking one product, across every location.
        sku : Optional[str]
            Exact-match filter on `sku`. The rows tracking one SKU — the identity used when an item has no product id.
        on_hand : Optional[float]
            Exact-match filter on `on_hand`. Exact balance, which is rarely what a reader wants: `?on_hand=0` finds the rows that are empty. There is no range filter here — GET /inventories/reorder-alerts is the "running low" question.
        reserved : Optional[float]
            Exact-match filter on `reserved`. Exact reserved quantity. `?reserved=0` finds the rows nothing is holding.
        reorder_point : Optional[float]
            Exact-match filter on `reorder_point`. The available quantity at or below which this row belongs on the replenishment worklist (GET /inventories/reorder-alerts).
        metadata : Optional[str]
            Exact-match filter on `metadata`. Free-form data the tenant keeps on this stock row, and ONE key this app reads: `backorder`. The WHOLE jsonb document is compared, serialized as JSON — this is equality, not a key lookup or a containment query, and a value that does not parse is answered 400.
        created_at : Optional[str]
            Exact-match filter on `created_at`. When the row was created.
        updated_at : Optional[str]
            Exact-match filter on `updated_at`. When this row was last written.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/stock'
        api_params = {}

        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)
        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if location_id is not None:
            api_params['location_id'] = self._normalize_value(location_id)
        if product_id is not None:
            api_params['product_id'] = self._normalize_value(product_id)
        if sku is not None:
            api_params['sku'] = self._normalize_value(sku)
        if on_hand is not None:
            api_params['on_hand'] = self._normalize_value(on_hand)
        if reserved is not None:
            api_params['reserved'] = self._normalize_value(reserved)
        if reorder_point is not None:
            api_params['reorder_point'] = self._normalize_value(reorder_point)
        if metadata is not None:
            api_params['metadata'] = self._normalize_value(metadata)
        if created_at is not None:
            api_params['created_at'] = self._normalize_value(created_at)
        if updated_at is not None:
            api_params['updated_at'] = self._normalize_value(updated_at)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def inventories_stock_create(
        self,
        location_id: str,
        metadata: Optional[Dict[str, Any]] = None,
        product_id: Optional[str] = None,
        reorder_point: Optional[float] = None,
        sku: Optional[str] = None
    ) -> Error:
        """
        Registers an item at a location. The row is born at ZERO and never gets a balance from this call: `on_hand` and `reserved` are NOT accepted, because they are the running total of the movements ledger, so an opening balance is a receipt (POST /inventories/receive) rather than a field here, and the only thing that ever moves either number afterwards is another booking. What this row carries is its identity (location + `product_id`/`sku`), its `reorder_point` and its metadata. `location_id` is the only field a create cannot omit; every other column is optional or defaulted by the database. The one rule that is a CHECK rather than a column is that a row has to identify its item, so `product_id` or `sku` has to be there as well. Mostly you do not need this route at all — every stock call creates the row it is missing — and a second row for an item this location already tracks is answered 409: no unique index enforces one row per item per location, so that row would split the item's balance across two rows the write routes cannot tell apart, each of them updating whichever the database returns first. That guard is a check before the insert and not a constraint, so it closes a double click or a re-run import and does not claim to close a race between two simultaneous creates.

        Parameters
        ----------
        location_id : str
            The location this balance is held at — a `locations` row of this tenant (GET /inventories/locations). There is ONE stock row per (location, item): the same SKU in three warehouses is three rows, and what a storefront shows is their sum (POST /inventories/availability). Deleting the location deletes its stock rows with it. It has to exist already (GET /inventories/locations); an id no location carries is answered 400 by the foreign key, not 404.
        metadata : Optional[Dict[str, Any]]
            Free-form data the tenant keeps on this stock row, and ONE key this app reads: `backorder`. A literal boolean `true` there opts this item into backorders while `backorder_policy` is 'allow_per_sku' — anything else, including the string "true", does not, and the reservation is refused with 422. That is how a merchant backorders the supplier-stocked half of a catalogue without promising the rest.
        product_id : Optional[str]
            The product this row tracks, as the products app knows it. A row tracks a `product_id` or a `sku` — the database insists on at least one (CHECK `product_id is not null or sku is not null`) — and matching is exact: a row keyed by SKU is not found by product id.
        reorder_point : Optional[float]
            The available quantity at or below which this row belongs on the replenishment worklist (GET /inventories/reorder-alerts). Null falls back to the `reorder_point_default` setting, so replenishment works without a threshold per SKU; 0 never alerts, which is how one row opts out.
        sku : Optional[str]
            The article number this row tracks when there is no product id, which is the normal case for an ERP-stocked catalogue. Exact match, and the identity every stock call may use instead of a uuid.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/stock'
        api_params = {}
        if location_id is None:
            raise RevenexxException('Missing required parameter: "location_id"')


        api_params['location_id'] = self._normalize_value(location_id)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['product_id'] = self._normalize_value(product_id)
        api_params['reorder_point'] = self._normalize_value(reorder_point)
        api_params['sku'] = self._normalize_value(sku)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def inventories_stock_delete(
        self,
        id: str
    ) -> Error:
        """
        Stops tracking one item at one location. A stock level is ONE item at ONE location, and it carries two numbers, neither of which is the sellable one: `on_hand` is what is physically there INCLUDING everything already promised, and `reserved` is what has been promised — it never reduces `on_hand`. What may still be sold is their difference, and it is derived on read and never stored, so there is no `available` column to read, filter or order by. A deleted balance is not recoverable: the ledger is the audit trail, not the source of truth, and nothing in this app ever replays it to rebuild a number — so the next receipt for the same item here creates a FRESH row at zero, standing next to movements that say otherwise. That used to be a trap a caller discovered afterwards. It is a stated property now, because the route REFUSES while the row still holds anything, and answers 409 with what it holds. The two things that block are the location delete's two, asked of one row. A reservation still `active` against this item at this location is the sharper one: /release and /commit look their stock row up by (location, item) on the very next call and would find nothing, so the hold would lower no `reserved` and /commit would book the whole quantity as a shortfall — orphaned immediately rather than eventually. `on_hand` above zero is the stronger one: deleting a LOCATION at least meant "close this warehouse" and took the balances as a side effect of the cascade, while this row IS the balance, so the delete can only ever mean "no longer tracked here" — true once the number is zero and a lie while it is not. POST /inventories/stock/{id}/adjust to zero is the operation that makes it true, and it BOOKS the movement, so the stock leaves through the ledger instead of vanishing with the row. Nothing points at it by foreign key, so the database takes nothing else with it. History therefore never blocks and is never deleted — the ledger is keyed on (location, item) and never on this id, so its bookings survive a row that is gone, BY DESIGN, exactly as they survive a location that is gone.

        Parameters
        ----------
        id : str
            The stock row.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/stock/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def inventories_stock_get(
        self,
        id: str
    ) -> Error:
        """
        A stock level is ONE item at ONE location, and it carries two numbers, neither of which is the sellable one: `on_hand` is what is physically there INCLUDING everything already promised, and `reserved` is what has been promised — it never reduces `on_hand`. What may still be sold is their difference, and it is derived on read and never stored, so there is no `available` column to read, filter or order by. Read it to see one item's position at one place, and to get the id the two row-scoped routes take: POST /inventories/stock/{id}/adjust corrects this balance, and GET /inventories/reorder-alerts reports it by this id. What it does not answer is how the balance got here — that is GET /inventories/movements filtered by the location and item on this row, because a movement points at (location, item) and never at a stock row id.

        Parameters
        ----------
        id : str
            The stock row.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/stock/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def inventories_stock_update(
        self,
        id: str,
        location_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        product_id: Optional[str] = None,
        reorder_point: Optional[float] = None,
        sku: Optional[str] = None
    ) -> Error:
        """
        Partial update of everything on the row EXCEPT its balance: reorder_point, metadata, identity. on_hand and reserved are dropped from the body — every stock change is a movement, and a body carrying nothing else is answered 422 with the route that was meant (POST /inventories/stock/{id}/adjust).

        Parameters
        ----------
        id : str
            The stock row.
        location_id : Optional[str]
            The location this balance is held at — a `locations` row of this tenant (GET /inventories/locations). There is ONE stock row per (location, item): the same SKU in three warehouses is three rows, and what a storefront shows is their sum (POST /inventories/availability). Deleting the location deletes its stock rows with it. It has to exist already (GET /inventories/locations); an id no location carries is answered 400 by the foreign key, not 404.
        metadata : Optional[Dict[str, Any]]
            Free-form data the tenant keeps on this stock row, and ONE key this app reads: `backorder`. A literal boolean `true` there opts this item into backorders while `backorder_policy` is 'allow_per_sku' — anything else, including the string "true", does not, and the reservation is refused with 422. That is how a merchant backorders the supplier-stocked half of a catalogue without promising the rest.
        product_id : Optional[str]
            The product this row tracks, as the products app knows it. A row tracks a `product_id` or a `sku` — the database insists on at least one (CHECK `product_id is not null or sku is not null`) — and matching is exact: a row keyed by SKU is not found by product id.
        reorder_point : Optional[float]
            The available quantity at or below which this row belongs on the replenishment worklist (GET /inventories/reorder-alerts). Null falls back to the `reorder_point_default` setting, so replenishment works without a threshold per SKU; 0 never alerts, which is how one row opts out.
        sku : Optional[str]
            The article number this row tracks when there is no product id, which is the normal case for an ERP-stocked catalogue. Exact match, and the identity every stock call may use instead of a uuid.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/stock/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if location_id is not None:
            api_params['location_id'] = self._normalize_value(location_id)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['product_id'] = self._normalize_value(product_id)
        api_params['reorder_point'] = self._normalize_value(reorder_point)
        api_params['sku'] = self._normalize_value(sku)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def inventories_stock_adjust(
        self,
        id: str,
        quantity: float,
        reason: Optional[str] = None
    ) -> Error:
        """
        Corrects the balance of ONE stock row, and only that one. It is the row-scoped twin of POST /inventories/adjust: the row already knows its location and item, so a caller owes nothing but a SIGNED delta on `on_hand` — positive to add, negative to take away — and a reason for it. The delta is not written onto the balance either; it is booked into the movements ledger as an `adjustment` and the balance follows, which is why the answer hands back the row at its new value instead of an acknowledgement. This is the route that replaced the Cockpit's editable on_hand field.

        Parameters
        ----------
        id : str
            The stock row to correct.
        quantity : float
            The SIGNED correction to this row's `on_hand`: −3 writes off three, +3 finds three. A delta, not the new balance. Zero is refused (400). A correction that would take `on_hand` below zero is a 422 the database insists on; one that would take it below this row's own `reserved` is a 422 the `allow_negative_stock` setting can permit.
        reason : Optional[str]
            Why this row is being corrected, written onto the ledger booking. Owed unless `movement_reason_required` is 'none'.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/stock/{id}/adjust'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        if quantity is None:
            raise RevenexxException('Missing required parameter: "quantity"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['quantity'] = self._normalize_value(quantity)
        api_params['reason'] = self._normalize_value(reason)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def inventories_vocabularies_list(
        self
    ) -> InventoryVocabularyIndex:
        """
        Discovery for the vocabulary routes: the enums this app publishes, each with its name, its title and its description and deliberately WITHOUT its values, so finding out what exists costs one small call and not one per vocabulary. Names: location-types, movement-types, reservation-statuses. Fetch one with GET /inventories/vocabularies/{name}; a client holding the qualified pair 'inventories.<name>' builds that URL from the pair alone.

        Returns
        -------
        InventoryVocabularyIndex
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/vocabularies'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=InventoryVocabularyIndex)


    def inventories_vocabularies_get(
        self,
        name: InventoriesVocabulariesGetName
    ) -> Error:
        """
        One vocabulary in full: every permitted value, each carrying the title and description a person reads for it and the badge tone a UI colours it with, so a client renders a status or a movement type without a hard-coded table of its own. The values are read out of the column's CHECK constraint, so the served set IS the enforced set and the two cannot drift — a value added to the constraint appears here even before anyone labels it, titled from its own key. Values come back in constraint order, which is lifecycle order for a status. 'closed' says the set is exhaustive, so a value outside it is stale data rather than a missing label. Names: location-types, movement-types, reservation-statuses.

        Parameters
        ----------
        name : InventoriesVocabulariesGetName
            The vocabulary name — the part after the dot in the qualified id. One of: location-types, movement-types, reservation-statuses. Anything else is a 404, so the enum is the complete set and not a suggestion.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/vocabularies/{name}'
        api_params = {}
        if name is None:
            raise RevenexxException('Missing required parameter: "name"')

        api_path = api_path.replace('{name}', str(self._normalize_value(name)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)

