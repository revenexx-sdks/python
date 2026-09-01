from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..enums.order_status import OrderStatus;
from ..enums.order_payment_status import OrderPaymentStatus;
from ..enums.order_fulfillment_status import OrderFulfillmentStatus;
from ..models.error import Error;
from ..models.order_number_ranges_seeded import OrderNumberRangesSeeded;
from ..models.order_item_create_request import OrderItemCreateRequest;
from ..models.order_customer_rollup_response import OrderCustomerRollupResponse;
from ..models.order_vocabulary_index import OrderVocabularyIndex;
from ..enums.orders_vocabularies_get_name import OrdersVocabulariesGetName;
from ..enums.order_comment_visibility import OrderCommentVisibility;
from ..models.order_cancel_position import OrderCancelPosition;
from ..models.order_return_position import OrderReturnPosition;
from ..enums.order_return_settlement import OrderReturnSettlement;
from ..enums.order_return_refusal import OrderReturnRefusal;
from ..models.order_shipment_position import OrderShipmentPosition;

class Orders(Service):

    def __init__(self, client) -> None:
        super(Orders, self).__init__(client)

    def orders_list(
        self,
        id: Optional[str] = None,
        number: Optional[str] = None,
        customer_order_number: Optional[str] = None,
        external_ref: Optional[str] = None,
        acknowledged_at: Optional[str] = None,
        cart_id: Optional[str] = None,
        contact_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        channel_id: Optional[str] = None,
        currency: Optional[str] = None,
        status: Optional[OrderStatus] = None,
        payment_status: Optional[OrderPaymentStatus] = None,
        fulfillment_status: Optional[OrderFulfillmentStatus] = None,
        on_hold: Optional[bool] = None,
        hold_reason: Optional[str] = None,
        item_count: Optional[float] = None,
        subtotal: Optional[float] = None,
        shipping_total: Optional[float] = None,
        tax_total: Optional[float] = None,
        grand_total: Optional[float] = None,
        placed_at: Optional[str] = None,
        completed_at: Optional[str] = None,
        cancelled_at: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        The route behind every order overview: the open orders of one customer, everything on hold, everything a market placed last week, or the one order somebody is quoting a number for (?number=ORD-000123 — the number is not the id, and this is how one becomes the other). The order LIST: the order rows without their positions, shipments, returns or cancellations — read GET /orders/{id} for the aggregate of one. Every parameter below is an exact match on the column it names, and combining them is an AND. Two kinds of key are not offered: one that names NO column is dropped silently, so a mistyped ?stauts=placed answers 200 with the whole list (compare the 'filter' echo against what you sent — no status code reports it), and the jsonb columns buyer, billing_address, shipping_address, payment, shipping, user_data and metadata reach the database as a text comparison and answer 400 invalid_value for anything that is not a whole JSON document.

        Parameters
        ----------
        id : Optional[str]
            Filter to exactly one order. GET /orders/{id} is the direct form and answers the aggregate; this exists because the list honours it too. Primary key of the order, and the id every other route takes. Not the order number.
        number : Optional[str]
            Look an order up by its NUMBER — the one filter a service desk starts from, and the way to turn the number a customer quotes into the uuid every other route wants. Exact match; there is no substring search on this API. The order number a human quotes — drawn from the tenant's order range at place-time, unique per tenant and never reused. It is NOT the id: every route addresses an order by uuid, and GET /orders?number=… is how a number becomes one.
        customer_order_number : Optional[str]
            Look an order up by the BUYER's own PO number. Not unique: the same buyer reference can legitimately sit on several orders. The BUYER's own reference — their purchase-order number. Free text, not unique, never generated here: it exists so the paperwork can carry the number the buyer's accounts payable will look for. One of the few fields PUT /orders/{id} may still change.
        external_ref : Optional[str]
            Find the order behind a reference in the fulfilling system — the ERP order number. Exact match, and null on everything not yet acknowledged. The FULFILLING system's reference for this order, typically the ERP order number. Written once by POST /orders/{id}/acknowledge and null until an integration acknowledged it.
        acknowledged_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When the fulfilling system took the order over. Written once. While it is null the order can still be modified here; afterwards modification goes through that system, unless the tenant sets allow_modification_after_acknowledge.
        cart_id : Optional[str]
            Find the order a given cart became. The reverse of the carts hand-over, and how a storefront checks whether a checkout already went through. The cart this order was placed from, when a storefront handed one over. A reference across an app boundary (the carts app), not a foreign key — nothing here checks that it resolves. Null for an order an integration or an operator created.
        contact_id : Optional[str]
            Filter to one person's orders — their order history. The PERSON who ordered — a contact in the customers app. Resolved from the acting principal whenever the caller carries one, and a body value that disagrees is refused rather than silently overridden. Null for a guest checkout.
        organization_id : Optional[str]
            Filter to one company's orders, across everyone who ordered for it. The B2B view, and the same attribution orders.reports.customer-rollup aggregates by. The COMPANY the order is booked on — an organization in the customers app, and the B2B half of who ordered. This is what orders.reports.customer-rollup aggregates by and what makes an order visible to a buyer's colleagues. Null on a private or guest order, which the rollup counts separately because it cannot attribute it.
        channel_id : Optional[str]
            Filter to rows whose `channel_id` is exactly this value. The sales channel the order arrived through — webshop, app, phone desk, EDI. Null when the caller named none.
        currency : Optional[str]
            Filter by ISO 4217 code. Worth remembering before summing `grand_total` over a mixed list: nothing on an order is ever converted. ISO 4217 code of EVERY amount on this order. Frozen at place-time from the market's default_currency unless the caller named one. Nothing on this order is ever converted, and the approval threshold is read in this currency — which is why the threshold is a per-market setting.
        status : Optional[OrderStatus]
            Filter by lifecycle status. `pending` IS the approval queue — there is no second entity for it. Where the order stands in its LIFECYCLE, and one of three independent status dimensions. 'pending' = created but not placed, an order waiting for approval; 'placed' = accepted, nothing shipped; 'in_fulfillment' = part of it has gone out, or all of it has and the tenant does not close on shipment; 'completed' and 'cancelled' end it. Moved by the action routes only — it is not writable through PUT /orders/{id}.
        payment_status : Optional[OrderPaymentStatus]
            Filter by the payment dimension, independently of the lifecycle: `payment_status=open&status=completed` is the delivered-but-unpaid list. Whether the order is PAID, and the dimension this app does not decide: it is fed from outside through POST /orders/{id}/payment-status (the payments app or an ERP), and only seeded at place-time from payment.status. Orthogonal to the lifecycle — a completed order can still be open, and a paid one can still be pending.
        fulfillment_status : Optional[OrderFulfillmentStatus]
            Filter by the derived shipping dimension. `unfulfilled` with `status=placed` is the work queue a warehouse picks from. Whether the order has SHIPPED, and the one dimension nobody writes: it is DERIVED after every quantity change from the positions' own bookkeeping. 'fulfilled' means shipped >= ordered − cancelled across all positions, 'partial' means something went out. Sending it has no effect; ship, cancel or return something and it moves.
        on_hold : Optional[bool]
            Filter to the held orders — the list somebody has to work through before anything of theirs can ship. A business stop, ORTHOGONAL to status: a held order keeps its lifecycle state and is refused at the guards. How far the hold reaches is the tenant's call (on_hold_blocks: shipping only, shipping and cancellation, or nothing at all).
        hold_reason : Optional[str]
            Filter to rows whose `hold_reason` is exactly this value. Why the order is held, in the words the shipping guard quotes back. Null when it is not held — releasing a hold clears it.
        item_count : Optional[float]
            Filter to rows whose `item_count` is exactly this value. The summed ORDERED quantity over all positions, rounded to a whole number — a headline figure for a list, computed once at place-time. It is deliberately not reduced when something is cancelled or returned; the positions carry that arithmetic.
        subtotal : Optional[float]
            Filter to rows whose `subtotal` is exactly this value. NET total of the positions (the sum of their line_total), COMPUTED here at place-time. In `currency`, four decimal places. A caller cannot set it.
        shipping_total : Optional[float]
            Filter to rows whose `shipping_total` is exactly this value. NET shipping cost, taken from shipping.price or, when the snapshot carries no price, from the request's shipping_total. In `currency`.
        tax_total : Optional[float]
            Filter to rows whose `tax_total` is exactly this value. All tax on this order: the positions' tax_amount plus the tax on shipping (shipping_total × shipping.tax_rate). COMPUTED here — a caller cannot set it.
        grand_total : Optional[float]
            Filter to rows whose `grand_total` is exactly this value. What the buyer owes: subtotal + shipping_total + tax_total, COMPUTED by this app and NEVER taken from the caller — trusting a supplied total is how inconsistent orders happened. This is the number the approval threshold is compared against and the number the revenue rollup sums.
        placed_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When the order was PLACED. Null while it is pending approval: an order awaiting sign-off exists but was never placed, and that is exactly the difference this field records.
        completed_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When the order was closed — by a full shipment, by payment or by hand, depending on the tenant's auto_complete_on. Null until then.
        cancelled_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When the order was cancelled, whether by a full cancel or by the last open quantity being cancelled position by position. Null otherwise.
        created_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When the order row was written. For a placed order this is placed_at; for a requested one it is when the request was submitted.
        updated_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When any column of the order last changed — every status move, every re-derived fulfillment, every modification.
        limit : Optional[float]
            Page size (default 50, max 200). A larger value is clamped to 200 rather than refused.
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending, the direction is lower case, and the column has to exist — the value reaches the data plane verbatim and anything else is a 400.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders'
        api_params = {}

        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if number is not None:
            api_params['number'] = self._normalize_value(number)
        if customer_order_number is not None:
            api_params['customer_order_number'] = self._normalize_value(customer_order_number)
        if external_ref is not None:
            api_params['external_ref'] = self._normalize_value(external_ref)
        if acknowledged_at is not None:
            api_params['acknowledged_at'] = self._normalize_value(acknowledged_at)
        if cart_id is not None:
            api_params['cart_id'] = self._normalize_value(cart_id)
        if contact_id is not None:
            api_params['contact_id'] = self._normalize_value(contact_id)
        if organization_id is not None:
            api_params['organization_id'] = self._normalize_value(organization_id)
        if channel_id is not None:
            api_params['channel_id'] = self._normalize_value(channel_id)
        if currency is not None:
            api_params['currency'] = self._normalize_value(currency)
        if status is not None:
            api_params['status'] = self._normalize_value(status)
        if payment_status is not None:
            api_params['payment_status'] = self._normalize_value(payment_status)
        if fulfillment_status is not None:
            api_params['fulfillment_status'] = self._normalize_value(fulfillment_status)
        if on_hold is not None:
            api_params['on_hold'] = self._normalize_value(on_hold)
        if hold_reason is not None:
            api_params['hold_reason'] = self._normalize_value(hold_reason)
        if item_count is not None:
            api_params['item_count'] = self._normalize_value(item_count)
        if subtotal is not None:
            api_params['subtotal'] = self._normalize_value(subtotal)
        if shipping_total is not None:
            api_params['shipping_total'] = self._normalize_value(shipping_total)
        if tax_total is not None:
            api_params['tax_total'] = self._normalize_value(tax_total)
        if grand_total is not None:
            api_params['grand_total'] = self._normalize_value(grand_total)
        if placed_at is not None:
            api_params['placed_at'] = self._normalize_value(placed_at)
        if completed_at is not None:
            api_params['completed_at'] = self._normalize_value(completed_at)
        if cancelled_at is not None:
            api_params['cancelled_at'] = self._normalize_value(cancelled_at)
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

        return response


    def orders_number_ranges_list(
        self,
        id: Optional[str] = None,
        code: Optional[str] = None,
        prefix: Optional[str] = None,
        suffix: Optional[str] = None,
        padding: Optional[float] = None,
        counter: Optional[float] = None,
        step: Optional[float] = None,
        position_step: Optional[float] = None,
        channel_id: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        The counters this tenant numbers its orders, delivery notes and returns from — what an operator sees on the Number ranges settings page, and what a migration reads to check the prefixes and the padding before it imports anything. Every parameter below is an exact-match filter on the column it names (?code=order finds the order counter). Two things are not: a key that names NO column is dropped silently — the call answers 200 with the unfiltered page, so compare the 'filter' echo against what you sent — and the jsonb column 'metadata' is honoured by the router but refused by the database (400 invalid_value) unless the value is a whole JSON document, which is why it is not offered here. It does not draw a number: `counter` is the last number DRAWN, and only placing an order, a shipment or a return moves it.

        Parameters
        ----------
        id : Optional[str]
            Filter to rows whose `id` is exactly this value. Primary key of the number range.
        code : Optional[str]
            Look a range up by its code — 'order', 'delivery', 'return', or whatever a settings key points at. Which counter this is, in the app's own words: 'order' numbers orders, 'delivery' numbers delivery notes, 'return' numbers returns. Unique per tenant, and the value the order_number_range_code / delivery_number_range_code / return_number_range_code settings point at — a setting naming a code no range carries is the 422 'number_range_missing'.
        prefix : Optional[str]
            Filter to rows whose `prefix` is exactly this value. Literal text in front of the counter: 'ORD-' turns counter 123 into ORD-000123. Empty by default.
        suffix : Optional[str]
            Filter to rows whose `suffix` is exactly this value. Literal text after the counter — a market or year marker on merchants who number that way. Empty by default, which is what most of them use.
        padding : Optional[float]
            Filter to rows whose `padding` is exactly this value. How wide the counter is written, zero-padded: 6 makes 123 into 000123. 0 writes the bare number. Widening it later does not renumber what was already drawn.
        counter : Optional[float]
            Filter to rows whose `counter` is exactly this value. The last number DRAWN — state, not configuration. The next draw is counter + step and writes the new value back, so moving this forward skips numbers and moving it back re-issues them (and the unique index then answers 409).
        step : Optional[float]
            Filter to rows whose `step` is exactly this value. How far the counter moves per draw. 1 is consecutive numbering; a larger step is what a merchant chooses who does not want their order volume readable off an invoice.
        position_step : Optional[float]
            Filter to rows whose `position_step` is exactly this value. The gap between the position numbers of a new order: 10 numbers the lines 10, 20, 30 — room to slot a line in between later without renumbering the rest. Read from the ORDER range only.
        channel_id : Optional[str]
            Filter to rows whose `channel_id` is exactly this value. The sales channel this range was created for, as a label. It does NOT select the range: a draw finds the range by `code` alone, and the unique index (tenant, code) means one code is one range per tenant — so an order on another channel draws from the same range this one names. Null on the three seeded ranges, which is every tenant-wide range.
        created_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When the range was created.
        updated_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When the range last changed — which includes every single number draw, because a draw writes the counter.
        limit : Optional[float]
            Page size (default 50, max 200). A larger value is clamped to 200 rather than refused.
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending, the direction is lower case, and the column has to exist — the value reaches the data plane verbatim and anything else is a 400.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/number-ranges'
        api_params = {}

        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if code is not None:
            api_params['code'] = self._normalize_value(code)
        if prefix is not None:
            api_params['prefix'] = self._normalize_value(prefix)
        if suffix is not None:
            api_params['suffix'] = self._normalize_value(suffix)
        if padding is not None:
            api_params['padding'] = self._normalize_value(padding)
        if counter is not None:
            api_params['counter'] = self._normalize_value(counter)
        if step is not None:
            api_params['step'] = self._normalize_value(step)
        if position_step is not None:
            api_params['position_step'] = self._normalize_value(position_step)
        if channel_id is not None:
            api_params['channel_id'] = self._normalize_value(channel_id)
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

        return response


    def orders_number_ranges_create(
        self,
        code: str,
        channel_id: Optional[str] = None,
        counter: Optional[float] = None,
        metadata: Optional[Dict[str, Any]] = None,
        padding: Optional[float] = None,
        position_step: Optional[float] = None,
        prefix: Optional[str] = None,
        step: Optional[float] = None,
        suffix: Optional[str] = None
    ) -> Error:
        """
        Add a counter beyond the three a tenant is seeded with, and give it the shape a merchant's numbers actually have: {prefix}{counter padded to `padding`}{suffix}, moving by `step` per draw. A new range is what the order_number_range_code / delivery_number_range_code / return_number_range_code settings can then be pointed at — the code is the name those settings use, and a setting naming a code no range carries makes placing an order answer 422. `code` is unique per tenant, so this is a 409 for one that is taken rather than a second counter under the same name. It does not renumber anything that already exists, and setting `counter` to a value already issued re-issues those numbers, which the unique index on the order number then refuses.

        Parameters
        ----------
        code : str
            Which counter this is, in the app's own words: 'order' numbers orders, 'delivery' numbers delivery notes, 'return' numbers returns. Unique per tenant, and the value the order_number_range_code / delivery_number_range_code / return_number_range_code settings point at — a setting naming a code no range carries is the 422 'number_range_missing'.
        channel_id : Optional[str]
            The sales channel this range was created for, as a label. It does NOT select the range: a draw finds the range by `code` alone, and the unique index (tenant, code) means one code is one range per tenant — so an order on another channel draws from the same range this one names. Null on the three seeded ranges, which is every tenant-wide range.
        counter : Optional[float]
            The last number DRAWN — state, not configuration. The next draw is counter + step and writes the new value back, so moving this forward skips numbers and moving it back re-issues them (and the unique index then answers 409). Defaults to 0, so the first number drawn is step.
        metadata : Optional[Dict[str, Any]]
            Free-form data for the caller. This app stores it and returns it, and reads nothing out of it.
        padding : Optional[float]
            How wide the counter is written, zero-padded: 6 makes 123 into 000123. 0 writes the bare number. Widening it later does not renumber what was already drawn. Defaults to 6.
        position_step : Optional[float]
            The gap between the position numbers of a new order: 10 numbers the lines 10, 20, 30 — room to slot a line in between later without renumbering the rest. Read from the ORDER range only. Defaults to 10.
        prefix : Optional[str]
            Literal text in front of the counter: 'ORD-' turns counter 123 into ORD-000123. Empty by default. Defaults to ''.
        step : Optional[float]
            How far the counter moves per draw. 1 is consecutive numbering; a larger step is what a merchant chooses who does not want their order volume readable off an invoice. Defaults to 1.
        suffix : Optional[str]
            Literal text after the counter — a market or year marker on merchants who number that way. Empty by default, which is what most of them use. Defaults to ''.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/number-ranges'
        api_params = {}
        if code is None:
            raise RevenexxException('Missing required parameter: "code"')


        if channel_id is not None:
            api_params['channel_id'] = self._normalize_value(channel_id)
        api_params['code'] = self._normalize_value(code)
        if counter is not None:
            api_params['counter'] = self._normalize_value(counter)
        if metadata is not None:
            api_params['metadata'] = self._normalize_value(metadata)
        if padding is not None:
            api_params['padding'] = self._normalize_value(padding)
        if position_step is not None:
            api_params['position_step'] = self._normalize_value(position_step)
        if prefix is not None:
            api_params['prefix'] = self._normalize_value(prefix)
        if step is not None:
            api_params['step'] = self._normalize_value(step)
        if suffix is not None:
            api_params['suffix'] = self._normalize_value(suffix)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_number_ranges_defaults(
        self
    ) -> OrderNumberRangesSeeded:
        """
        Make sure the three codes this app draws from exist: 'order' (ORD-), 'delivery' (DEL-) and 'return' (RET-), each padded to six digits and stepping by one. The app runs it for you on install, so a fresh tenant needs nothing; call it by hand after a range was deleted, or to check what a tenant has. Idempotent: a code that already exists comes back under 'existing' and is left EXACTLY as it is, counter included, so a merchant who changed the prefix keeps their change. Answers 200, never 201 — it is a reconcile, not a create — and it never repairs or renames a range that is already there.

        Returns
        -------
        OrderNumberRangesSeeded
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/number-ranges/defaults'
        api_params = {}

        response = self.client.call('post', api_path, {
        }, api_params)

        return self._parse_response(response, model=OrderNumberRangesSeeded)


    def orders_number_ranges_delete(
        self,
        id: str
    ) -> Error:
        """
        Remove a counter a tenant no longer numbers anything from. It touches nothing that was numbered out of it: existing orders, delivery notes and returns keep the numbers they were given, because a number is copied onto the row at place-time and is not a reference to this table. Deleting one of the three standard codes is allowed and is usually a mistake — the next draw against it answers 422 'number_range_missing', unless POST /orders/number-ranges/defaults or a reinstall seeds it again, which starts its counter back at 0.

        Parameters
        ----------
        id : str
            The number range id (uuid).
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/number-ranges/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_number_ranges_get(
        self,
        id: str
    ) -> Error:
        """
        One counter with its whole configuration: the prefix and suffix around the number, how wide it is padded, how far each draw moves it, where it currently stands, and the position_step new order lines are numbered in. Reach for it when you hold the id — from the list, or from what a create answered — and want the row as it stands now. Reading does not draw a number and does not move `counter`; the id is the range's uuid, not its `code`, and a code is turned into a range through GET /orders/number-ranges?code=order.

        Parameters
        ----------
        id : str
            The number range id (uuid).
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/number-ranges/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_number_ranges_update(
        self,
        id: str,
        channel_id: Optional[str] = None,
        code: Optional[str] = None,
        counter: Optional[float] = None,
        metadata: Optional[Dict[str, Any]] = None,
        padding: Optional[float] = None,
        position_step: Optional[float] = None,
        prefix: Optional[str] = None,
        step: Optional[float] = None,
        suffix: Optional[str] = None
    ) -> Error:
        """
        Change the format or the state of an existing counter: a new prefix or suffix, a wider padding, a different step, a different position_step for new order lines — or `counter` itself, which is state rather than configuration. Everything takes effect on the NEXT draw only: nothing that was already numbered is renumbered, so widening the padding leaves ORD-000123 and starts writing ORD-0000124. Moving `counter` forward skips numbers, and moving it back re-issues numbers that exist, which the unique index on the order number answers 409 for at place-time rather than here. Renaming `code` to one another range of this tenant already holds is a 409.

        Parameters
        ----------
        id : str
            The number range id (uuid).
        channel_id : Optional[str]
            The sales channel this range was created for, as a label. It does NOT select the range: a draw finds the range by `code` alone, and the unique index (tenant, code) means one code is one range per tenant — so an order on another channel draws from the same range this one names. Null on the three seeded ranges, which is every tenant-wide range.
        code : Optional[str]
            Which counter this is, in the app's own words: 'order' numbers orders, 'delivery' numbers delivery notes, 'return' numbers returns. Unique per tenant, and the value the order_number_range_code / delivery_number_range_code / return_number_range_code settings point at — a setting naming a code no range carries is the 422 'number_range_missing'.
        counter : Optional[float]
            The last number DRAWN — state, not configuration. The next draw is counter + step and writes the new value back, so moving this forward skips numbers and moving it back re-issues them (and the unique index then answers 409). Defaults to 0, so the first number drawn is step.
        metadata : Optional[Dict[str, Any]]
            Free-form data for the caller. This app stores it and returns it, and reads nothing out of it.
        padding : Optional[float]
            How wide the counter is written, zero-padded: 6 makes 123 into 000123. 0 writes the bare number. Widening it later does not renumber what was already drawn. Defaults to 6.
        position_step : Optional[float]
            The gap between the position numbers of a new order: 10 numbers the lines 10, 20, 30 — room to slot a line in between later without renumbering the rest. Read from the ORDER range only. Defaults to 10.
        prefix : Optional[str]
            Literal text in front of the counter: 'ORD-' turns counter 123 into ORD-000123. Empty by default. Defaults to ''.
        step : Optional[float]
            How far the counter moves per draw. 1 is consecutive numbering; a larger step is what a merchant chooses who does not want their order volume readable off an invoice. Defaults to 1.
        suffix : Optional[str]
            Literal text after the counter — a market or year marker on merchants who number that way. Empty by default, which is what most of them use. Defaults to ''.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/number-ranges/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if channel_id is not None:
            api_params['channel_id'] = self._normalize_value(channel_id)
        if code is not None:
            api_params['code'] = self._normalize_value(code)
        if counter is not None:
            api_params['counter'] = self._normalize_value(counter)
        if metadata is not None:
            api_params['metadata'] = self._normalize_value(metadata)
        if padding is not None:
            api_params['padding'] = self._normalize_value(padding)
        if position_step is not None:
            api_params['position_step'] = self._normalize_value(position_step)
        if prefix is not None:
            api_params['prefix'] = self._normalize_value(prefix)
        if step is not None:
            api_params['step'] = self._normalize_value(step)
        if suffix is not None:
            api_params['suffix'] = self._normalize_value(suffix)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_place(
        self,
        items: List[OrderItemCreateRequest],
        billing_address: Optional[Dict[str, Any]] = None,
        buyer: Optional[Dict[str, Any]] = None,
        cart_id: Optional[str] = None,
        channel_id: Optional[str] = None,
        contact_id: Optional[str] = None,
        currency: Optional[str] = None,
        customer_order_number: Optional[str] = None,
        grand_total: Optional[float] = None,
        metadata: Optional[Dict[str, Any]] = None,
        organization_id: Optional[str] = None,
        payment: Optional[Dict[str, Any]] = None,
        shipping: Optional[Dict[str, Any]] = None,
        shipping_address: Optional[Dict[str, Any]] = None,
        shipping_total: Optional[float] = None,
        user_data: Optional[Dict[str, Any]] = None
    ) -> Error:
        """
        The way an order comes into existence — the call a checkout, a punch-out or an ERP import makes once the basket is final. The body is a SNAPSHOT: items with their product copies, plus the buyer, the addresses and the payment and shipping choices frozen as they were at this moment, so the order stays readable when the catalogue or the customer changes underneath it. The app draws the order number from the tenant's order range, numbers the positions, computes subtotal, tax and grand_total from the lines, and writes the order.placed event that carries the order onto the bus. It does not reserve stock, take payment or talk to an ERP: those are separate capabilities, and this route's job ends when the event is on the bus. Two things can turn a placement into a REQUEST awaiting approval, and both still answer 201 — with status='pending' and no placed_at: a principal holding only orders.request, and an order worth more than the tenant's require_approval_above_value (a principal holding orders.approve is exempt from the threshold). The order.requested event says which, in 'approval_reason'. The currency defaults to the market's default_currency setting and the position cap is the tenant's max_items_per_order.

        Parameters
        ----------
        items : List[OrderItemCreateRequest]
            The order positions — at least one, and at most the tenant's max_items_per_order (500 out of the box; a longer list is a 400 naming the limit).
        billing_address : Optional[Dict[str, Any]]
            The invoice address, FROZEN at place-time. Changing the customer's address afterwards does not change what this order was billed to.
        buyer : Optional[Dict[str, Any]]
            The ordering party as it was at place-time, FROZEN: a copy, not a reference, so the order still reads correctly after the customer record is renamed, merged or deleted. The caller decides what goes in; this app stores it and reads nothing out of it.
        cart_id : Optional[str]
            The cart this order was placed from, when a storefront handed one over. A reference across an app boundary (the carts app), not a foreign key — nothing here checks that it resolves. Null for an order an integration or an operator created. The carts.order hand-over sets it.
        channel_id : Optional[str]
            The sales channel the order arrived through — webshop, app, phone desk, EDI. Null when the caller named none.
        contact_id : Optional[str]
            The PERSON who ordered — a contact in the customers app. Resolved from the acting principal whenever the caller carries one, and a body value that disagrees is refused rather than silently overridden. Null for a guest checkout. Ignored when the caller carries a principal — the RESOLVED contact wins, and a body value that disagrees is a 400 rather than a silent override.
        currency : Optional[str]
            ISO 4217 code of EVERY amount on this order. Frozen at place-time from the market's default_currency unless the caller named one. Nothing on this order is ever converted, and the approval threshold is read in this currency — which is why the threshold is a per-market setting. Defaults to the market's default_currency setting.
        customer_order_number : Optional[str]
            The BUYER's own reference — their purchase-order number. Free text, not unique, never generated here: it exists so the paperwork can carry the number the buyer's accounts payable will look for. One of the few fields PUT /orders/{id} may still change.
        grand_total : Optional[float]
            Optional, and CHECKED rather than used: the order always computes its own total from the positions, the shipping cost and the tax. Send it as a checksum on that arithmetic — if it agrees the order is placed, and if it disagrees the call is refused with 400 naming both numbers, yours and the computed one. The comparison is at 2 decimal places (this app stores 4, ERPs work to 2, so a difference below a cent is agreement). It is never taken as the order value: the approval threshold and the revenue rollup read the computed number, which is why a total that disagrees is an error rather than an override.
        metadata : Optional[Dict[str, Any]]
            Free-form data belonging to the INTEGRATION side — an ERP's own bookkeeping about this order. Stored and returned untouched; nothing here reads it.
        organization_id : Optional[str]
            The COMPANY the order is booked on — an organization in the customers app, and the B2B half of who ordered. This is what orders.reports.customer-rollup aggregates by and what makes an order visible to a buyer's colleagues. Null on a private or guest order, which the rollup counts separately because it cannot attribute it. A principal's own organization wins over this when it has one.
        payment : Optional[Dict[str, Any]]
            The payment arrangement as it was chosen, FROZEN. This app reads exactly two keys and stores the rest untouched: 'status' seeds payment_status at place-time when it names one of the permitted values (anything else is ignored and the order starts 'open'), and 'payment_id' is merged in by POST /orders/{id}/payment-status. The method itself, its provider fields and any redirect state belong to the payments app.
        shipping : Optional[Dict[str, Any]]
            The shipping arrangement as it was chosen, FROZEN. Two keys are READ at place-time and feed the totals: 'price' becomes shipping_total (the shipping_total field is only the fallback when this is absent) and 'tax_rate' is what shipping is taxed at, because shipping is a Nebenleistung and is taxed too. Everything else — the carrier product, the delivery window, the pickup point — is stored untouched and belongs to the shipping app.
        shipping_address : Optional[Dict[str, Any]]
            The delivery address, FROZEN at place-time — what goes on the label of every shipment of this order. Null on an order that is never delivered (a service, a digital item, a collection).
        shipping_total : Optional[float]
            NET shipping cost, taken from shipping.price or, when the snapshot carries no price, from the request's shipping_total. In `currency`. Only read when the shipping snapshot carries no 'price'.
        user_data : Optional[Dict[str, Any]]
            Free-form data belonging to the ORDERING side — carried through from the storefront or the cart and handed back untouched. One of the few fields PUT /orders/{id} may still change.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/place'
        api_params = {}
        if items is None:
            raise RevenexxException('Missing required parameter: "items"')


        api_params['billing_address'] = self._normalize_value(billing_address)
        api_params['buyer'] = self._normalize_value(buyer)
        api_params['cart_id'] = self._normalize_value(cart_id)
        api_params['channel_id'] = self._normalize_value(channel_id)
        api_params['contact_id'] = self._normalize_value(contact_id)
        api_params['currency'] = self._normalize_value(currency)
        api_params['customer_order_number'] = self._normalize_value(customer_order_number)
        api_params['grand_total'] = self._normalize_value(grand_total)
        api_params['items'] = self._normalize_value(items)
        api_params['metadata'] = self._normalize_value(metadata)
        api_params['organization_id'] = self._normalize_value(organization_id)
        api_params['payment'] = self._normalize_value(payment)
        api_params['shipping'] = self._normalize_value(shipping)
        api_params['shipping_address'] = self._normalize_value(shipping_address)
        api_params['shipping_total'] = self._normalize_value(shipping_total)
        api_params['user_data'] = self._normalize_value(user_data)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_reports_customer_rollup(
        self,
        as_of: Optional[str] = None,
        cursor: Optional[str] = None,
        organization_ids: Optional[List[str]] = None,
        statuses: Optional[List[OrderStatus]] = None
    ) -> OrderCustomerRollupResponse:
        """
        What each company has bought, as numbers another app can keep: order count, lifetime revenue, first and last order date, and the same count and revenue over the last 30, 90 and 365 days. This is what a customer segment like "bought for more than 100k last year" is built on, and the customers app materialises it into a local projection its segment rules query. It answers about ORGANIZATIONS only — a private or guest order carries none and is counted in orders_without_organization rather than attributed to anybody — and it converts nothing, so an organization that ordered in two currencies gets both listed and one summed number to read with care. Revenue lives in orders, customer segments live in the customers app, and the two may not join (ADR-0055: no cross-app FK, grant or view). This capability is the hand-over. Every number is additive (count/sum/min/max) so partial answers merge; the average order value is deliberately not returned — it is revenue_total / order_count over the merged parts. Windows are anchored at as_of, which is echoed back so a loop measures one consistent picture.

        Parameters
        ----------
        as_of : Optional[str]
            Anchor for the rolling windows (default now). Pin it and send it back on every call of a loop, otherwise the windows drift by the duration of the loop.
        cursor : Optional[str]
            Continue an unfinished scan: the exact value the previous call returned, which is the id of the last order it read. Do not construct one — it is a resume point, not an offset. Omit it on the first call. It is honoured in BOTH call shapes, organization_ids included: send the whole batch again alongside it whenever `done` came back false, or the part of the batch after the cursor is simply never read.
        organization_ids : Optional[List[str]]
            Roll up exactly these organizations and no others — at most 200, because the ids travel to the data plane as one in.() filter. Naming them does NOT make the answer complete by itself: the scan is the same paged, time-budgeted loop either way, so a batch with more orders than one page can still stop early with `done: false` and a cursor. Small batches finish in one call, which is the normal case, but check `done` rather than assume it. Omitted = scan every order and answer for every organization that appears on one.
        statuses : Optional[List[OrderStatus]]
            Which lifecycle statuses count as revenue. Defaults to placed, in_fulfillment and completed: a pending order was never placed, and a cancelled one is not revenue. Widening this is how a merchant who books on approval gets their own definition of the same numbers.
        
        Returns
        -------
        OrderCustomerRollupResponse
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/reports/customer-rollup'
        api_params = {}

        api_params['as_of'] = self._normalize_value(as_of)
        api_params['cursor'] = self._normalize_value(cursor)
        api_params['organization_ids'] = self._normalize_value(organization_ids)
        api_params['statuses'] = self._normalize_value(statuses)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=OrderCustomerRollupResponse)


    def orders_vocabularies_list(
        self
    ) -> OrderVocabularyIndex:
        """
        Which value sets this app will describe for you, by name — order statuses, payment statuses, fulfillment statuses, item types, return statuses and return resolutions — so a client can discover them instead of shipping its own copy of five statuses that goes stale one release later. The values themselves are deliberately NOT here: this is the index, and each set is fetched on its own. Discovery for the vocabulary routes. Names: cancellation-scopes, comment-visibilities, fulfillment-statuses, item-types, payment-statuses, return-resolutions, return-statuses, statuses. Fetch one with GET /orders/vocabularies/{name}; a client holding the qualified pair 'orders.<name>' builds that URL from the pair alone. 'title' and 'description' are locale maps wherever somebody wrote the copy and plain strings where the fallback did — read both forms.

        Returns
        -------
        OrderVocabularyIndex
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/vocabularies'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=OrderVocabularyIndex)


    def orders_vocabularies_get(
        self,
        name: OrdersVocabulariesGetName
    ) -> Error:
        """
        Everything a UI needs to render one of this app's value sets without knowing it: every permitted value, in order, each with a title and description in the locales somebody wrote and a badge tone to colour it. Fetch it once and a status filter, a status badge and a resolution picker all stay correct through a lifecycle change, because the set served IS the set enforced. It answers about values, not about rows — nothing here says how many orders are in a status. The values are read out of the column's CHECK constraint, so the served set IS the enforced set and the two cannot drift — a value added to the constraint appears here even before anyone labels it, titled from its own key. Values come back in constraint order, which is lifecycle order for a status, and 'final' marks the values that END the lifecycle (completed, cancelled) so a client can ask "is this order still open?" instead of matching names it guessed. Every set is exhaustive ('closed' is always true); 'source' says who enforces it — 'schema' for a CHECK constraint, 'app' for 'return-resolutions', whose column carries none and whose words the return routes enforce instead. Those values additionally carry 'stage' (complete | reject): the transition that accepts them. 'title' and 'description' are locale maps where the copy was written and plain strings where the key-derived fallback answered, on the vocabulary and on every value alike. Names: cancellation-scopes, comment-visibilities, fulfillment-statuses, item-types, payment-statuses, return-resolutions, return-statuses, statuses.

        Parameters
        ----------
        name : OrdersVocabulariesGetName
            The vocabulary name — the part after the dot in the qualified id.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/vocabularies/{name}'
        api_params = {}
        if name is None:
            raise RevenexxException('Missing required parameter: "name"')

        api_path = api_path.replace('{name}', str(self._normalize_value(name)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_get(
        self,
        id: str
    ) -> Error:
        """
        The single source of order information, and what an order detail screen is built from: the order row plus its positions, its shipments with the shipment_items each one booked, its returns and its cancellations — one call, no assembling five lists. A cancellation's and a return's 'positions' are ARRAYS of {order_item_id, quantity}; a return's entries additionally carry 'restock'. Two things it does not carry: the comments and the event trail, which are their own paginated routes because both grow without bound. Addressed by uuid — an order number goes through GET /orders?number=… first.

        Parameters
        ----------
        id : str
            The order id (uuid). This segment reaches a uuid column: an order NUMBER is not accepted here — filter GET /orders by ?number= to resolve one.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_update(
        self,
        id: str,
        billing_address: Optional[Dict[str, Any]] = None,
        buyer: Optional[Dict[str, Any]] = None,
        customer_order_number: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        shipping_address: Optional[Dict[str, Any]] = None,
        user_data: Optional[Dict[str, Any]] = None
    ) -> Error:
        """
        The narrow correction window a service desk needs: the customer gave the wrong delivery address, the buyer's name is misspelled, their purchase-order number was missing. Six columns and no others — customer_order_number, buyer, billing_address, shipping_address, user_data and metadata — and each is REPLACED whole, not merged, so send the entire address rather than the one line that changed. It moves nothing: status, payment_status, fulfillment_status and the quantities belong to the action routes, and a body carrying them is accepted with those keys quietly dropped. The window closes when the fulfilling system acknowledges the order, because from then on the ERP holds the copy that ships — unless the tenant set allow_modification_after_acknowledge. Every accepted change writes an order.updated event naming the columns it touched.

        Parameters
        ----------
        id : str
            The order id (uuid). This segment reaches a uuid column: an order NUMBER is not accepted here — filter GET /orders by ?number= to resolve one.
        billing_address : Optional[Dict[str, Any]]
            The invoice address, FROZEN at place-time. Changing the customer's address afterwards does not change what this order was billed to. Replaced wholesale — send the whole address, not a patch of it.
        buyer : Optional[Dict[str, Any]]
            The ordering party as it was at place-time, FROZEN: a copy, not a reference, so the order still reads correctly after the customer record is renamed, merged or deleted. The caller decides what goes in; this app stores it and reads nothing out of it. Replaced wholesale — send the whole snapshot, not a patch of it.
        customer_order_number : Optional[str]
            The BUYER's own reference — their purchase-order number. Free text, not unique, never generated here: it exists so the paperwork can carry the number the buyer's accounts payable will look for. One of the few fields PUT /orders/{id} may still change.
        metadata : Optional[Dict[str, Any]]
            Free-form data belonging to the INTEGRATION side — an ERP's own bookkeeping about this order. Stored and returned untouched; nothing here reads it. Replaced wholesale.
        shipping_address : Optional[Dict[str, Any]]
            The delivery address, FROZEN at place-time — what goes on the label of every shipment of this order. Null on an order that is never delivered (a service, a digital item, a collection). Replaced wholesale. This is the one correction that actually matters after placement: the label of every shipment still to go out is printed from it.
        user_data : Optional[Dict[str, Any]]
            Free-form data belonging to the ORDERING side — carried through from the storefront or the cart and handed back untouched. One of the few fields PUT /orders/{id} may still change. Replaced wholesale.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if billing_address is not None:
            api_params['billing_address'] = self._normalize_value(billing_address)
        if buyer is not None:
            api_params['buyer'] = self._normalize_value(buyer)
        if customer_order_number is not None:
            api_params['customer_order_number'] = self._normalize_value(customer_order_number)
        if metadata is not None:
            api_params['metadata'] = self._normalize_value(metadata)
        if shipping_address is not None:
            api_params['shipping_address'] = self._normalize_value(shipping_address)
        if user_data is not None:
            api_params['user_data'] = self._normalize_value(user_data)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_acknowledge(
        self,
        id: str,
        external_ref: Optional[str] = None
    ) -> Error:
        """
        The return channel for whatever fulfils the order. An Integration Studio workflow picks up order.placed, books the order into the ERP, and calls this with the id the ERP gave it — which lands in external_ref and makes the two systems mutually findable. It stamps acknowledged_at from the server's clock, and that timestamp is what closes the correction window: PUT /orders/{id} refuses afterwards, because the copy that ships now lives elsewhere. It is a handshake and nothing more — it does not change status, payment_status or fulfillment_status, and it does not ship anything. Once only: a second call is a 422 rather than a silent overwrite of the first system's reference.

        Parameters
        ----------
        id : str
            The order id (uuid). This segment reaches a uuid column: an order NUMBER is not accepted here — filter GET /orders by ?number= to resolve one.
        external_ref : Optional[str]
            The FULFILLING system's reference for this order, typically the ERP order number. Written once by POST /orders/{id}/acknowledge and null until an integration acknowledged it. Keeps the existing value when omitted.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/{id}/acknowledge'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if external_ref is not None:
            api_params['external_ref'] = self._normalize_value(external_ref)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_cancel(
        self,
        id: str,
        cancelled_by: Optional[str] = None,
        reason: Optional[str] = None
    ) -> Error:
        """
        Call the whole order off: every position's full quantity is booked as cancelled, the order moves to 'cancelled', a cancellation record is written with the reason and who gave it, and an order.cancelled event goes onto the bus. Only while NOTHING has shipped — once a single position has gone out the order is partly real and this answers 422; take the remaining quantities off with POST /orders/{id}/items/cancel instead, and handle what already shipped as a return. It refunds nothing and returns nothing to stock: payment travels through /payment-status and restocking is an explicit inventories call by the orchestrator. A tenant may require a reason (cancel_requires_reason), and a hold may block it (on_hold_blocks = 'shipping_and_cancel').

        Parameters
        ----------
        id : str
            The order id (uuid). This segment reaches a uuid column: an order NUMBER is not accepted here — filter GET /orders by ?number= to resolve one.
        cancelled_by : Optional[str]
            Who cancelled, as the caller reported it — an operator, a desk, a system. Free text; this app does not resolve it against a user directory.
        reason : Optional[str]
            Why it was cancelled, free text. Mandatory when the tenant sets cancel_requires_reason — for those merchants an unexplained cancellation is refused with a 400.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/{id}/cancel'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if cancelled_by is not None:
            api_params['cancelled_by'] = self._normalize_value(cancelled_by)
        if reason is not None:
            api_params['reason'] = self._normalize_value(reason)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_comments_list(
        self,
        id: str,
        id_query: Optional[str] = None,
        body: Optional[str] = None,
        visibility: Optional[OrderCommentVisibility] = None,
        author: Optional[str] = None,
        created_at: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Error:
        """
        What people have written about this order, oldest first: the service desk's own notes and the messages meant for the customer, in one list. Filter by ?visibility=customer to build the version a customer may see, and by ?visibility=internal for the desk's own — the route does NOT decide that for you, so a customer-facing surface has to ask for the customer ones. Comments are prose about the order and never move it; the lifecycle lives in the event trail. Every parameter below is an exact match on the column it names. `order_id` is deliberately absent: the route fixes it from the path AFTER the query filter is read, so sending one is accepted and then overwritten — it filters nothing. DEPRECATED KEY: the response also repeats 'items' under 'comments' for compatibility with the pre-envelope shape. It is the same array; read 'items'. The alias is removed in the next minor version.

        Parameters
        ----------
        id : str
            The order id (uuid). This segment reaches a uuid column: an order NUMBER is not accepted here — filter GET /orders by ?number= to resolve one.
        id_query : Optional[str]
            Filter to rows whose `id` is exactly this value. Primary key of the comment.
        body : Optional[str]
            Filter to rows whose `body` is exactly this value. The comment itself. Plain text; this app neither renders nor sanitizes it.
        visibility : Optional[OrderCommentVisibility]
            Filter to internal notes or to the customer-visible ones. `visibility=customer` is what a customer order view should read. Who may see it: 'internal' is a note between operators, 'customer' is meant to be shown in the customer's order view. Nothing here enforces that — this app labels the comment and the client showing it decides. Defaults to the tenant's default_comment_visibility.
        author : Optional[str]
            Filter by exact author, as it was reported. Free text — this is not resolved against a user directory, so it matches only what was written. Who wrote it, as the caller reported it. Free text; not resolved against a user directory.
        created_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When the comment was written. Comments come back oldest first.
        limit : Optional[float]
            Page size (default 50, max 200). A larger value is clamped to 200 rather than refused.
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending, the direction is lower case, and the column has to exist — the value reaches the data plane verbatim and anything else is a 400.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/{id}/comments'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if id_query is not None:
            api_params['id'] = self._normalize_value(id_query)
        if body is not None:
            api_params['body'] = self._normalize_value(body)
        if visibility is not None:
            api_params['visibility'] = self._normalize_value(visibility)
        if author is not None:
            api_params['author'] = self._normalize_value(author)
        if created_at is not None:
            api_params['created_at'] = self._normalize_value(created_at)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_comments_create(
        self,
        id: str,
        body: str,
        author: Optional[str] = None,
        visibility: Optional[OrderCommentVisibility] = None
    ) -> Error:
        """
        Write down what happened that the state machine cannot record: what the customer said on the phone, why an exception was made, what the warehouse found in the box. `visibility` decides who the note is for — 'internal' for the service desk, 'customer' for text meant to be shown to the buyer — and it defaults to the tenant's default_comment_visibility, which is 'internal' out of the box, so a note is never accidentally customer-facing. Adding one writes an order.comment.added event, so the trail shows that a note was made and its visibility, without copying the text onto the bus. It changes nothing about the order, and it sends nothing to anybody: this stores a comment, it does not email the customer.

        Parameters
        ----------
        id : str
            The order id (uuid). This segment reaches a uuid column: an order NUMBER is not accepted here — filter GET /orders by ?number= to resolve one.
        body : str
            The comment itself. Plain text; this app neither renders nor sanitizes it.
        author : Optional[str]
            Who wrote it, as the caller reported it. Free text; not resolved against a user directory.
        visibility : Optional[OrderCommentVisibility]
            Who may see it: 'internal' is a note between operators, 'customer' is meant to be shown in the customer's order view. Nothing here enforces that — this app labels the comment and the client showing it decides. Defaults to the tenant's default_comment_visibility. Defaults to the tenant's default_comment_visibility setting, which is 'internal' out of the box.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/{id}/comments'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        if body is None:
            raise RevenexxException('Missing required parameter: "body"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if author is not None:
            api_params['author'] = self._normalize_value(author)
        api_params['body'] = self._normalize_value(body)
        if visibility is not None:
            api_params['visibility'] = self._normalize_value(visibility)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_complete(
        self,
        id: str,
        completed_by: Optional[str] = None
    ) -> Error:
        """
        Declare the order finished, whatever the quantities say — the service was delivered, the download was fetched, or an operator has decided the rest is not coming. status moves to 'completed' and completed_at is stamped from the server's clock. It does NOT ship anything or change the quantities, so fulfillment_status stays whatever the positions make it, and an order completed with lines still open shows exactly that. A completed order is final: modification, shipping and cancellation all refuse afterwards, and only a return may still be registered against it. The counterpart of auto_complete_on = 'payment' | 'manual': something has to close an order that shipping no longer closes by itself, and it is also the honest end for a service or digital order that never ships. Writes an order_events row 'order.completed' with via='manual'.

        Parameters
        ----------
        id : str
            The order id (uuid). This segment reaches a uuid column: an order NUMBER is not accepted here — filter GET /orders by ?number= to resolve one.
        completed_by : Optional[str]
            Who closed the order, as the caller reports it. Not stored on the order: it is carried in the order.completed event's payload, which is where the audit trail keeps who did what. Free text, not resolved against a user directory.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/{id}/complete'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if completed_by is not None:
            api_params['completed_by'] = self._normalize_value(completed_by)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_events_list(
        self,
        id: str,
        id_query: Optional[str] = None,
        name: Optional[str] = None,
        actor: Optional[str] = None,
        created_at: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Error:
        """
        Everything that has ever happened to this order, oldest first: placed or requested, updated, acknowledged, shipped, held, paid, returned, completed, cancelled — each with the payload the action carried. This is the audit trail an operator reads to answer "why is this order in this state", and it is the same row the platform publishes as a domain event, so what a workflow reacted to and what a person sees here cannot diverge. It is append-only and this route is read-only: rows are written by the action routes and there is no way to add, edit or remove one. An order's trail grows for as long as the order lives, so it is paginated like every other list — 'page.hasMore' says whether more of it exists. Every parameter below is an exact match on the column it names; `order_id` is deliberately absent, because the route fixes it from the path after the query filter is read and a value sent for it is overwritten rather than honoured. The jsonb column 'payload' is not offered for the same reason it is not offered on the order list: the data plane answers 400 for anything that is not a whole JSON document. DEPRECATED KEY: the response also repeats 'items' under 'events' for compatibility with the pre-envelope shape. It is the same array; read 'items'. The alias is removed in the next minor version.

        Parameters
        ----------
        id : str
            The order id (uuid). This segment reaches a uuid column: an order NUMBER is not accepted here — filter GET /orders by ?number= to resolve one.
        id_query : Optional[str]
            Filter to rows whose `id` is exactly this value. Primary key of the event row.
        name : Optional[str]
            Filter the trail to one kind of event — `order.shipment.created` for the dispatch history, `order.return.completed` for the settled returns. WHAT happened, and this is the domain event: the manifest emits order_event.created on insert and this value is the event name on the bus. The names this app writes are order.placed, order.requested, order.updated, order.acknowledged, order.cancelled, order.item.cancelled, order.shipment.created, order.completed, order.held, order.unheld, order.payment_status.changed, order.comment.added, order.return.registered, order.return.received, order.return.completed and order.return.rejected.
        actor : Optional[str]
            Filter to the events one principal caused. Only order.placed and order.requested carry an actor, so this filters to those two names by construction. Who caused it: the resolved contact id of the acting principal. Only order.placed and order.requested carry one today — every other row is null — so filtering on it filters to those two names. The database constrains nothing here (the column is text); the uuid shape is what this app WRITES, which is also why no example is published: no id an app invents names a row a tenant holds.
        created_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When it happened. The trail comes back oldest first, which is the order a human reads a history in.
        limit : Optional[float]
            Page size (default 50, max 200). A larger value is clamped to 200 rather than refused.
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending, the direction is lower case, and the column has to exist — the value reaches the data plane verbatim and anything else is a 400.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/{id}/events'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if id_query is not None:
            api_params['id'] = self._normalize_value(id_query)
        if name is not None:
            api_params['name'] = self._normalize_value(name)
        if actor is not None:
            api_params['actor'] = self._normalize_value(actor)
        if created_at is not None:
            api_params['created_at'] = self._normalize_value(created_at)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_hold(
        self,
        id: str,
        reason: Optional[str] = None
    ) -> Error:
        """
        Stop an order from moving while a human sorts something out — a credit check, a suspected fraud, an address nobody can deliver to. It sets a flag with the reason attached, and the flag is deliberately ORTHOGONAL to the lifecycle: the order keeps its status, its payment status and its quantities, and appears on a worklist as 'held' rather than being pushed into a state it will have to come back out of. How far the hold reaches is the tenant's setting on_hold_blocks: shipping only, shipping and cancellation (the credit-check case, where the order must move in neither direction), or nothing at all, which leaves the flag advisory. Holding an order twice is allowed and simply replaces the reason; releasing it is POST /orders/{id}/unhold.

        Parameters
        ----------
        id : str
            The order id (uuid). This segment reaches a uuid column: an order NUMBER is not accepted here — filter GET /orders by ?number= to resolve one.
        reason : Optional[str]
            Why the order is held, in the words the shipping guard quotes back. Null when it is not held — releasing a hold clears it.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/{id}/hold'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if reason is not None:
            api_params['reason'] = self._normalize_value(reason)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_items_cancel(
        self,
        id: str,
        positions: List[OrderCancelPosition],
        cancelled_by: Optional[str] = None,
        reason: Optional[str] = None
    ) -> Error:
        """
        Take quantities off an order that is otherwise going ahead — three of the ten are discontinued, one line is out of stock and the customer would rather not wait. Each named quantity is booked onto its position as cancelled and guarded against the OPEN quantity (ordered − shipped − cancelled), so nothing already shipped can be cancelled away underneath a shipment. The order's fulfillment_status is re-derived afterwards, and when every position ends up fully cancelled the order itself moves to 'cancelled' — which is how this becomes a full cancel by arithmetic rather than by a second call. Positions are REQUIRED here, unlike on /ship and /return: cancelling an entire order by omitting a field is not something anybody should be able to do by accident; that is what POST /orders/{id}/cancel is for. Read GET /orders/{id}/shippable for the open quantity per position before calling.

        Parameters
        ----------
        id : str
            The order id (uuid). This segment reaches a uuid column: an order NUMBER is not accepted here — filter GET /orders by ?number= to resolve one.
        positions : List[OrderCancelPosition]
            The quantities to take off the order. Required here, unlike on /ship and /return: cancelling everything by default is not a thing anybody should be able to do by omission — that is what /cancel is for.
        cancelled_by : Optional[str]
            Who cancelled, as the caller reported it — an operator, a desk, a system. Free text; this app does not resolve it against a user directory.
        reason : Optional[str]
            Why it was cancelled, free text. Mandatory when the tenant sets cancel_requires_reason — for those merchants an unexplained cancellation is refused with a 400.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/{id}/items/cancel'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        if positions is None:
            raise RevenexxException('Missing required parameter: "positions"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if cancelled_by is not None:
            api_params['cancelled_by'] = self._normalize_value(cancelled_by)
        api_params['positions'] = self._normalize_value(positions)
        if reason is not None:
            api_params['reason'] = self._normalize_value(reason)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_payment_status_update(
        self,
        id: str,
        status: OrderPaymentStatus,
        payment_id: Optional[str] = None
    ) -> Error:
        """
        Payment is the one status dimension this app does not decide for itself: it is FED IN from whatever took the money — the payments app, a PSP webhook relayed by a workflow, or a finance clerk marking an invoice settled. This route writes that word onto the order and records the change as an order.payment_status.changed event carrying the previous value, so the trail shows the sequence and not just the current state. Optionally attach the payment_id of the transaction it came from. It takes no money, refunds none and validates nothing about the amount — it records a fact somebody else established, and any of the seven words may follow any other. The other half of auto_complete_on = 'payment': an order that has shipped in full is completed by this call when the status becomes 'paid'.

        Parameters
        ----------
        id : str
            The order id (uuid). This segment reaches a uuid column: an order NUMBER is not accepted here — filter GET /orders by ?number= to resolve one.
        status : OrderPaymentStatus
            The new value of the payment dimension. Whether the order is PAID, and the dimension this app does not decide: it is fed from outside through POST /orders/{id}/payment-status (the payments app or an ERP), and only seeded at place-time from payment.status. Orthogonal to the lifecycle — a completed order can still be open, and a paid one can still be pending.
        payment_id : Optional[str]
            The reference into the payment system. MERGED into the order's payment snapshot under 'payment_id' — the rest of the snapshot is left alone — and carried in the order.payment_status.changed event. Omitted leaves the snapshot untouched.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/{id}/payment-status'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        if status is None:
            raise RevenexxException('Missing required parameter: "status"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if payment_id is not None:
            api_params['payment_id'] = self._normalize_value(payment_id)
        api_params['status'] = self._normalize_value(status)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_return(
        self,
        id: str,
        metadata: Optional[Dict[str, Any]] = None,
        positions: Optional[List[OrderReturnPosition]] = None,
        reason: Optional[str] = None,
        restock: Optional[bool] = None
    ) -> Error:
        """
        Open a return case: the customer has announced goods are coming back, and this is where that becomes a tracked thing with a return number of its own, drawn from the tenant's return range. Positions are guarded against what actually SHIPPED and has not already come back, so a return cannot exceed the goods that left. Each position carries a `restock` flag saying whether the item is expected to be sellable again — recorded now, acted on only when the return completes. Omitting `positions` registers everything still returnable, the 'the customer sent the whole delivery back' case. Nothing is booked yet: quantity_returned stays where it is and the order does not move — the return starts as 'registered' and travels through receive and complete or reject. Allowed on a completed order, refused on a cancelled one.

        Parameters
        ----------
        id : str
            The order id (uuid). This segment reaches a uuid column: an order NUMBER is not accepted here — filter GET /orders by ?number= to resolve one.
        metadata : Optional[Dict[str, Any]]
            Free-form data for the caller — the returns portal's own reference. Stored and returned untouched.
        positions : Optional[List[OrderReturnPosition]]
            What is coming back. Omitted = every position with a returnable (shipped, not yet returned) quantity, in full.
        reason : Optional[str]
            Why the goods are coming back, free text as the customer or the desk stated it. Also what /reject stores when it is given no resolution out of the published set.
        restock : Optional[bool]
            The default restock flag for positions that carry none of their own — and the only way to say "put it all back into stock" when the positions are defaulted. It does not restock anything itself: it decides what the completion REPORTS for the orchestrator's inventories.restock call.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/{id}/return'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if metadata is not None:
            api_params['metadata'] = self._normalize_value(metadata)
        if positions is not None:
            api_params['positions'] = self._normalize_value(positions)
        if reason is not None:
            api_params['reason'] = self._normalize_value(reason)
        if restock is not None:
            api_params['restock'] = self._normalize_value(restock)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_returns_complete(
        self,
        id: str,
        rid: str,
        resolution: Optional[OrderReturnSettlement] = None
    ) -> Error:
        """
        Accept the return and close the case: the goods are taken back on the order's books and the settlement is recorded as one of the published words — refunded, credited, replaced and so on. This is the step a refund or a credit note hangs off, and the only step that moves quantity_returned. It does not refund money and does not put stock back itself: the answer's 'restock' array names what the orchestrator should hand to inventories.restock, and payment travels through /payment-status. Once completed the return is final — receive, complete and reject all refuse afterwards. The goods accounting moves here and nowhere else: quantity_returned is booked onto each position, completed_at is stamped by the SERVER, and positions flagged restock are reported back in the answer's 'restock' array for the orchestrator's inventories.restock call. 'resolution' is validated against the settlement words this app publishes (refund, partial_refund, replacement, repair, store_credit — see GET /orders/vocabularies/return-resolutions); anything else is refused rather than stored as a word no reader knows. It is checked before the positions are booked, so a rejected value leaves nothing behind.

        Parameters
        ----------
        id : str
            The order id (uuid). This segment reaches a uuid column: an order NUMBER is not accepted here — filter GET /orders by ?number= to resolve one.
        rid : str
            The return id (uuid). It must belong to the order in {id} — a return of another order is a 404, not a cross-order write.
        resolution : Optional[OrderReturnSettlement]
            How the return was settled. Omitted = settled without recording how.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/{id}/returns/{rid}/complete'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        if rid is None:
            raise RevenexxException('Missing required parameter: "rid"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))
        api_path = api_path.replace('{rid}', str(self._normalize_value(rid)))

        api_params['resolution'] = self._normalize_value(resolution)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_returns_receive(
        self,
        id: str,
        rid: str,
        data: Dict[str, Any]
    ) -> Error:
        """
        The goods-in scan: the parcel is physically back, warehouse staff have it in their hands, and nobody has decided yet whether the customer gets their money. It moves the return from 'registered' to 'received' and stamps received_at, which is what separates 'announced' from 'here' on a returns worklist. It books nothing — quantity_returned is written by the complete step and by nothing else — so a return that arrives damaged can still be rejected afterwards. Only a registered return can be received; a second call, or one against a settled return, is a 422. This step is skippable: a return may be completed straight from 'registered' where a merchant does not scan goods in.

        Parameters
        ----------
        id : str
            The order id (uuid). This segment reaches a uuid column: an order NUMBER is not accepted here — filter GET /orders by ?number= to resolve one.
        rid : str
            The return id (uuid). It must belong to the order in {id} — a return of another order is a 404, not a cross-order write.
        data : Dict[str, Any]
            Request body
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/{id}/returns/{rid}/receive'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        if rid is None:
            raise RevenexxException('Missing required parameter: "rid"')

        if data is None:
            raise RevenexxException('Missing required parameter: "data"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))
        api_path = api_path.replace('{rid}', str(self._normalize_value(rid)))

        api_params['data'] = self._normalize_value(data)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_returns_reject(
        self,
        id: str,
        rid: str,
        reason: Optional[str] = None,
        resolution: Optional[OrderReturnRefusal] = None
    ) -> Error:
        """
        Close the case against the customer: the goods came back used, outside the window, or were never covered in the first place. The return moves to 'rejected', rejected_at is stamped, and the refusal is recorded either as one of the published refusal words or as a sentence somebody wrote about this one return. The order is untouched — the quantities still count as shipped and not returned, which is the point: a rejected return must leave the books exactly as they were. Rejection is final, and it says nothing about where the physical goods go. Nothing is booked onto the positions. 'resolution' is validated against the refusal words (wear_and_tear, not_returnable); 'reason' stays free text — a sentence about this one return rather than a value out of a set — and is what is stored when no resolution is named.

        Parameters
        ----------
        id : str
            The order id (uuid). This segment reaches a uuid column: an order NUMBER is not accepted here — filter GET /orders by ?number= to resolve one.
        rid : str
            The return id (uuid). It must belong to the order in {id} — a return of another order is a 404, not a cross-order write.
        reason : Optional[str]
            Free-text fallback for 'resolution' — a sentence about this one return, not a value out of the set.
        resolution : Optional[OrderReturnRefusal]
            Why the return was refused.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/{id}/returns/{rid}/reject'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        if rid is None:
            raise RevenexxException('Missing required parameter: "rid"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))
        api_path = api_path.replace('{rid}', str(self._normalize_value(rid)))

        if reason is not None:
            api_params['reason'] = self._normalize_value(reason)
        api_params['resolution'] = self._normalize_value(resolution)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_ship(
        self,
        id: str,
        carrier: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        number: Optional[str] = None,
        positions: Optional[List[OrderShipmentPosition]] = None,
        shipped_at: Optional[str] = None,
        tracking_code: Optional[str] = None,
        tracking_url: Optional[str] = None
    ) -> Error:
        """
        Book goods out: which positions and how much of each, with the carrier and the tracking code that go to the customer. It draws a delivery-note number from the tenant's delivery range, books quantity_shipped onto every named position, re-derives the order's fulfillment_status from the arithmetic (unfulfilled → partial → fulfilled) and emits order.shipment.created. Omitting `positions` means everything still open, in full, which is the ordinary 'send the rest' case and the only one a UI without a line editor can express; the answer always names the quantities that actually went out. It does not print a label, buy postage or notify anybody — a shipping workflow reacts to the event. Whether a full shipment CLOSES the order is the tenant's call (setting auto_complete_on): 'shipment' completes it here, 'payment' leaves it in_fulfillment until payment_status becomes paid, 'manual' waits for orders.complete. The order.completed event follows the order, so it is only emitted when the order actually completed.

        Parameters
        ----------
        id : str
            The order id (uuid). This segment reaches a uuid column: an order NUMBER is not accepted here — filter GET /orders by ?number= to resolve one.
        carrier : Optional[str]
            Who is carrying it, in the merchant's own words. Free text — this app neither validates it nor knows the carrier's API.
        metadata : Optional[Dict[str, Any]]
            Free-form data for the caller — the warehouse system's own reference for this handover. Stored and returned untouched.
        number : Optional[str]
            The DELIVERY NOTE number — drawn from the tenant's delivery range, unique per tenant, and a different series from the order number. A caller may supply its own when the number is issued by the warehouse system instead. Drawn from the 'delivery' range when omitted; supply one only when the number is issued elsewhere.
        positions : Optional[List[OrderShipmentPosition]]
            What this shipment carries. Omitted = every position with an open quantity, in full. GET /orders/{id}/shippable answers exactly the budget each one is guarded against.
        shipped_at : Optional[str]
            When the goods actually left. Defaults to now, and a caller may backdate it — a shipment booked on Monday for a Friday handover says Friday.
        tracking_code : Optional[str]
            The consignment number the carrier issued. Free text: every carrier formats it differently and this app stores whatever it is given.
        tracking_url : Optional[str]
            Where a human can follow the parcel. Supplied by the caller — this app does not build it, because only the caller knows the carrier's tracking address.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/{id}/ship'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if carrier is not None:
            api_params['carrier'] = self._normalize_value(carrier)
        if metadata is not None:
            api_params['metadata'] = self._normalize_value(metadata)
        if number is not None:
            api_params['number'] = self._normalize_value(number)
        if positions is not None:
            api_params['positions'] = self._normalize_value(positions)
        if shipped_at is not None:
            api_params['shipped_at'] = self._normalize_value(shipped_at)
        if tracking_code is not None:
            api_params['tracking_code'] = self._normalize_value(tracking_code)
        if tracking_url is not None:
            api_params['tracking_url'] = self._normalize_value(tracking_url)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_shippable(
        self,
        id: str
    ) -> Error:
        """
        What a shipment dialog needs before it can offer anything: the open quantity per position, and one boolean saying whether a shipment would be accepted at all. Reach for it to fill a picking screen or to decide whether a 'create shipment' button is enabled, instead of subtracting the quantities client-side. It changes nothing and books nothing — it is the question POST /orders/{id}/ship answers with an action. The read half of orders.ship. The open quantity per position and the two guards (cancelled/completed order, hold) are the SAME code the ship route runs, so what this answers and what that accepts cannot drift — a client subtracting the quantities itself eventually offers a shipment the server refuses, or one it should have refused. 'shippable' is false with a 'blocked_reason' when the order is held, cancelled, completed or has nothing open.

        Parameters
        ----------
        id : str
            The order id (uuid). This segment reaches a uuid column: an order NUMBER is not accepted here — filter GET /orders by ?number= to resolve one.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/{id}/shippable'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def orders_unhold(
        self,
        id: str,
        data: Dict[str, Any]
    ) -> Error:
        """
        The whole of the release: the flag comes off, the reason is cleared, and an order.unheld event says the order may move again. Whatever the hold was blocking — shipping, and cancellation on tenants configured that way — is accepted from this call on. It restores nothing else and skips nothing: the order continues from exactly the status and quantities it had when it was held, and any shipping that was due meanwhile still has to be done by hand. An order that is not on hold answers 422 rather than pretending to release one, so this is safe to give to a worklist and not to a loop that calls it blindly.

        Parameters
        ----------
        id : str
            The order id (uuid). This segment reaches a uuid column: an order NUMBER is not accepted here — filter GET /orders by ?number= to resolve one.
        data : Dict[str, Any]
            Request body
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/orders/{id}/unhold'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        if data is None:
            raise RevenexxException('Missing required parameter: "data"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        api_params['data'] = self._normalize_value(data)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)

