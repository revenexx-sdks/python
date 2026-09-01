from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..models.error import Error;
from ..enums.inventories_reservations_list_status import InventoriesReservationsListStatus;
from ..models.reservation_sweep_result import ReservationSweepResult;
from ..models.inventory_stock_item import InventoryStockItem;

class InventoriesReservations(Service):

    def __init__(self, client) -> None:
        super(InventoriesReservations, self).__init__(client)

    def inventories_commit(
        self,
        order_ref: str
    ) -> Error:
        """
        Call this when the goods leave the building, and not before. Reserving only promised them — `reserved` went up and `on_hand` did not move, because the stock was still on the shelf; committing is the moment they are gone, so it lowers BOTH on each stock row and writes one `shipment` booking per hold, with a SIGNED negative quantity, as the ledger's record that they left. It takes the whole `order_ref` and every hold still active on it: there is no partial commit and no per-line id, so a part shipment means reserving the parts separately in the first place. It is also final — 'committed' ends the lifecycle and nothing moves a hold out of it, so goods coming back are POST /inventories/restock (a new receipt), never an undo of this. An order with nothing active is a 422 rather than a quiet zero, because it means the hold was already released or already shipped; /release answers the same situation with a 200 on purpose, since cancelling twice is harmless and shipping twice is not.

        Parameters
        ----------
        order_ref : str
            The order this hold belongs to. The caller supplies it — this app mints nothing — and it is the handle POST /inventories/release and POST /inventories/commit act on, so it has to be the same string the order carries elsewhere. At least one character (CHECK `length(order_ref) > 0`). Not unique: an order holds one reservation per item, and they are released or committed together. Every ACTIVE hold under this reference ships: `on_hand` and `reserved` both fall and a `shipment` booking is written for each. Unlike release, committing an order that has nothing active is a 422 — it means the hold was already released or already shipped, and shipping twice is worth saying out loud.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/commit'
        api_params = {}
        if order_ref is None:
            raise RevenexxException('Missing required parameter: "order_ref"')


        api_params['order_ref'] = self._normalize_value(order_ref)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def inventories_release(
        self,
        order_ref: str
    ) -> Error:
        """
        The cancellation end of the reserve → commit | release lifecycle: it takes an `order_ref`, ends every hold still active on it, gives the stock back and writes a 'release' booking for each one, exactly like the expiry sweeper. Idempotent: an order with nothing active answers released:0 — which is why it is a 200 and not the 422 commit answers.

        Parameters
        ----------
        order_ref : str
            The order this hold belongs to. The caller supplies it — this app mints nothing — and it is the handle POST /inventories/release and POST /inventories/commit act on, so it has to be the same string the order carries elsewhere. At least one character (CHECK `length(order_ref) > 0`). Not unique: an order holds one reservation per item, and they are released or committed together. Every ACTIVE hold under this reference is given back; ones already committed or released are left alone. A reference no reservation carries releases nothing and answers `released: 0` — not an error, which is what makes a retried cancellation safe.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/release'
        api_params = {}
        if order_ref is None:
            raise RevenexxException('Missing required parameter: "order_ref"')


        api_params['order_ref'] = self._normalize_value(order_ref)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def inventories_reservations_list(
        self,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None,
        id: Optional[str] = None,
        location_id: Optional[str] = None,
        product_id: Optional[str] = None,
        sku: Optional[str] = None,
        quantity: Optional[float] = None,
        order_ref: Optional[str] = None,
        status: Optional[InventoriesReservationsListStatus] = None,
        expires_at: Optional[str] = None,
        metadata: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None
    ) -> Error:
        """
        A reservation is stock promised to an `order_ref`. It is created only by POST /inventories/reserve and moved only by /commit, /release and the expiry sweep — there is no create, update or delete route, because the lifecycle IS the API. Only an 'active' hold counts towards a stock row's `reserved`; 'released' and 'committed' rows stay for the audit trail and hold nothing. This is the answer to "what is this order actually holding" (`?order_ref=…`) and to "what is holding this stock" (`?status=active&location_id=…`) — the second is the only way to see WHY a row's `reserved` is what it is, since a stock row reports the total and never who asked for it. `expires_at` filters on an exact timestamp and not a range, so this cannot answer "what expires today"; the deadline is acted on by POST /inventories/reservations/sweep, not by reading it here.

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
            Exact-match filter on `location_id`. The holds served by one location.
        product_id : Optional[str]
            Exact-match filter on `product_id`. The product being held, copied from the reserve call.
        sku : Optional[str]
            Exact-match filter on `sku`. The article number being held, copied from the reserve call.
        quantity : Optional[float]
            Exact-match filter on `quantity`. How much is being held, ALWAYS POSITIVE — the database CHECK is `quantity > 0`, because a hold of nothing is not a hold.
        order_ref : Optional[str]
            Exact-match filter on `order_ref`. Every hold an order carries. This is the lookup POST /inventories/release and /commit act on.
        status : Optional[InventoriesReservationsListStatus]
            Exact-match filter on `status`. Where the hold stands in the reserve → commit | release lifecycle. Only 'active' counts towards `reserved`, so `?status=active` is the set that is really holding stock.
        expires_at : Optional[str]
            Exact-match filter on `expires_at`. Exact deadline, not a range — this cannot answer "what expires today". The sweeper is what acts on deadlines (POST /inventories/reservations/sweep).
        metadata : Optional[str]
            Exact-match filter on `metadata`. Free-form, and one key this app writes itself: `backordered` — how much of this hold was not covered by stock on hand when it was taken. The WHOLE jsonb document is compared, serialized as JSON — this is equality, not a key lookup or a containment query, and a value that does not parse is answered 400.
        created_at : Optional[str]
            Exact-match filter on `created_at`. When the row was created.
        updated_at : Optional[str]
            Exact-match filter on `updated_at`. When the hold last changed — in practice, when it moved out of `active`..
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/reservations'
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
        if quantity is not None:
            api_params['quantity'] = self._normalize_value(quantity)
        if order_ref is not None:
            api_params['order_ref'] = self._normalize_value(order_ref)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if expires_at is not None:
            api_params['expires_at'] = self._normalize_value(expires_at)
        if metadata is not None:
            api_params['metadata'] = self._normalize_value(metadata)
        if created_at is not None:
            api_params['created_at'] = self._normalize_value(created_at)
        if updated_at is not None:
            api_params['updated_at'] = self._normalize_value(updated_at)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def inventories_reservations_sweep(
        self,
        data: Dict[str, Any]
    ) -> ReservationSweepResult:
        """
        The expiry sweeper, also run by the 'expire-reservations' schedule every 15 minutes. Releases reservations past their own expires_at and — once reservation_ttl_minutes is above 0 — reservations older than that lifetime which never carried a deadline. Each release gives the stock back and writes a 'release' booking, exactly like a cancellation. Idempotent: a second run finds nothing.

        Parameters
        ----------
        data : Dict[str, Any]
            Request body
        
        Returns
        -------
        ReservationSweepResult
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/reservations/sweep'
        api_params = {}
        if data is None:
            raise RevenexxException('Missing required parameter: "data"')


        api_params['data'] = self._normalize_value(data)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ReservationSweepResult)


    def inventories_reservations_get(
        self,
        id: str
    ) -> Error:
        """
        A reservation is stock promised to an `order_ref`. It is created only by POST /inventories/reserve and moved only by /commit, /release and the expiry sweep — there is no create, update or delete route, because the lifecycle IS the API. Only an 'active' hold counts towards a stock row's `reserved`; 'released' and 'committed' rows stay for the audit trail and hold nothing. One hold, with the three facts that are not on the order it belongs to: which location it was allocated to, when it expires, and — in `metadata.backordered` — how much of it was never covered by stock, which is how a promise made under a permissive backorder policy stays visible afterwards. The id is for reading only. Every transition acts on the whole `order_ref` (/commit, /release, the sweep), so there is no route that takes this id and no way to release one line of an order on its own.

        Parameters
        ----------
        id : str
            The reservation.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/inventories/reservations/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def inventories_reserve(
        self,
        order_ref: str,
        expires_at: Optional[str] = None,
        items: Optional[List[InventoryStockItem]] = None,
        location_code: Optional[str] = None,
        product_id: Optional[str] = None,
        quantity: Optional[float] = None,
        ship_to: Optional[Dict[str, Any]] = None,
        sku: Optional[str] = None
    ) -> Error:
        """
        Takes a hold against an `order_ref`, and plans the whole call before writing anything, so a reservation that cannot be satisfied changes nothing. WHICH location serves an item is not the caller's to choose: the tenant's allocation_strategy decides it ('priority', walking the enabled locations by their priority; 'nearest', matching ship_to against a location's country; or 'single_location' for the whole order); backorder_policy decides what happens when none can — refuse (422), or reserve anyway and let availability go negative. expires_at defaults from reservation_ttl_minutes and the sweeper enforces it.

        Parameters
        ----------
        order_ref : str
            The order this hold belongs to. The caller supplies it — this app mints nothing — and it is the handle POST /inventories/release and POST /inventories/commit act on, so it has to be the same string the order carries elsewhere. At least one character (CHECK `length(order_ref) > 0`). Not unique: an order holds one reservation per item, and they are released or committed together. Reserving twice under the same reference ADDS holds rather than replacing them — release first if you mean to replace.
        expires_at : Optional[str]
            When this hold lapses. The sweeper — POST /inventories/reservations/sweep, and the 'expire-reservations' schedule that runs it every 15 minutes — releases everything past this moment exactly as a cancellation would, so an abandoned checkout stops holding stock on its own. Null means the row named no deadline: it is swept on its AGE instead once `reservation_ttl_minutes` is above 0, which is what makes turning that setting on retroactive. Omit it to let the `reservation_ttl_minutes` setting stamp one (0 — its default — means no deadline at all); send one to hold this order for a window of its own, e.g. a quote that stands until Friday.
        items : Optional[List[InventoryStockItem]]
            The items to hold, at most 200 in one call — a whole cart in one request. The call is planned before anything is written, so either every item is placed or nothing is.
        location_code : Optional[str]
            Where a BACKORDERED item is booked when no location holds a stock row for it at all — the last fallback, not the allocator: which location serves an item that IS in stock comes from `allocation_strategy`. Omitted, the `default_location_code` setting decides.
        product_id : Optional[str]
            Inline single-item form: the product to move, instead of a one-entry `items` array. The two forms are equivalent — nothing downstream knows which arrived.
        quantity : Optional[float]
            Inline single-item form: how many to hold. Positive — the hold is expressed as a positive reservation, while the ledger booking it writes carries the negative.
        ship_to : Optional[Dict[str, Any]]
            Where the order is going. Read ONLY when the tenant's `allocation_strategy` is 'nearest' — under 'priority' or 'single_location' it is accepted and ignored, so sending it is never wrong, it is just not always heard.
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

        api_path = '/v1/inventories/reserve'
        api_params = {}
        if order_ref is None:
            raise RevenexxException('Missing required parameter: "order_ref"')


        api_params['expires_at'] = self._normalize_value(expires_at)
        if items is not None:
            api_params['items'] = self._normalize_value(items)
        api_params['location_code'] = self._normalize_value(location_code)
        api_params['order_ref'] = self._normalize_value(order_ref)
        api_params['product_id'] = self._normalize_value(product_id)
        api_params['quantity'] = self._normalize_value(quantity)
        if ship_to is not None:
            api_params['ship_to'] = self._normalize_value(ship_to)
        api_params['sku'] = self._normalize_value(sku)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)

