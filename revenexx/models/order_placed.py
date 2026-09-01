from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_fulfillment_status import OrderFulfillmentStatus
from .order_item import OrderItem
from ..enums.order_payment_status import OrderPaymentStatus
from ..enums.order_status import OrderStatus

class OrderPlaced(AppwriteModel):
    """
    The order that was created, with its positions. A placement has no shipments, returns or cancellations yet — read GET /orders/{id} for the aggregate.

    Attributes
    ----------
    acknowledged_at : Optional[str]
        When the fulfilling system took the order over. Written once. While it is null the order can still be modified here; afterwards modification goes through that system, unless the tenant sets allow_modification_after_acknowledge.
    billing_address : Optional[Dict[str, Any]]
        The invoice address, FROZEN at place-time. Changing the customer&#039;s address afterwards does not change what this order was billed to.
    buyer : Optional[Dict[str, Any]]
        The ordering party as it was at place-time, FROZEN: a copy, not a reference, so the order still reads correctly after the customer record is renamed, merged or deleted. The caller decides what goes in; this app stores it and reads nothing out of it.
    cancelled_at : Optional[str]
        When the order was cancelled, whether by a full cancel or by the last open quantity being cancelled position by position. Null otherwise.
    cart_id : Optional[str]
        The cart this order was placed from, when a storefront handed one over. A reference across an app boundary (the carts app), not a foreign key — nothing here checks that it resolves. Null for an order an integration or an operator created.
    channel_id : Optional[str]
        The sales channel the order arrived through — webshop, app, phone desk, EDI. Null when the caller named none.
    completed_at : Optional[str]
        When the order was closed — by a full shipment, by payment or by hand, depending on the tenant&#039;s auto_complete_on. Null until then.
    contact_id : Optional[str]
        The PERSON who ordered — a contact in the customers app. Resolved from the acting principal whenever the caller carries one, and a body value that disagrees is refused rather than silently overridden. Null for a guest checkout.
    created_at : Optional[str]
        When the order row was written. For a placed order this is placed_at; for a requested one it is when the request was submitted.
    currency : Optional[str]
        ISO 4217 code of EVERY amount on this order. Frozen at place-time from the market&#039;s default_currency unless the caller named one. Nothing on this order is ever converted, and the approval threshold is read in this currency — which is why the threshold is a per-market setting.
    customer_order_number : Optional[str]
        The BUYER&#039;s own reference — their purchase-order number. Free text, not unique, never generated here: it exists so the paperwork can carry the number the buyer&#039;s accounts payable will look for. One of the few fields PUT /orders/{id} may still change.
    external_ref : Optional[str]
        The FULFILLING system&#039;s reference for this order, typically the ERP order number. Written once by POST /orders/{id}/acknowledge and null until an integration acknowledged it.
    fulfillment_status : Optional[OrderFulfillmentStatus]
        Whether the order has SHIPPED, and the one dimension nobody writes: it is DERIVED after every quantity change from the positions&#039; own bookkeeping. &#039;fulfilled&#039; means shipped &gt;= ordered − cancelled across all positions, &#039;partial&#039; means something went out. Sending it has no effect; ship, cancel or return something and it moves.
    grand_total : Optional[float]
        What the buyer owes: subtotal + shipping_total + tax_total, COMPUTED by this app and NEVER taken from the caller — trusting a supplied total is how inconsistent orders happened. This is the number the approval threshold is compared against and the number the revenue rollup sums.
    hold_reason : Optional[str]
        Why the order is held, in the words the shipping guard quotes back. Null when it is not held — releasing a hold clears it.
    id : Optional[str]
        Primary key of the order, and the id every other route takes. Not the order number.
    item_count : Optional[float]
        The summed ORDERED quantity over all positions, rounded to a whole number — a headline figure for a list, computed once at place-time. It is deliberately not reduced when something is cancelled or returned; the positions carry that arithmetic.
    items : Optional[List[OrderItem]]
        The created positions, numbered in steps of the order range position_step unless the caller set them.
    metadata : Optional[Dict[str, Any]]
        Free-form data belonging to the INTEGRATION side — an ERP&#039;s own bookkeeping about this order. Stored and returned untouched; nothing here reads it.
    number : Optional[str]
        The order number a human quotes — drawn from the tenant&#039;s order range at place-time, unique per tenant and never reused. It is NOT the id: every route addresses an order by uuid, and GET /orders?number=… is how a number becomes one.
    on_hold : Optional[bool]
        A business stop, ORTHOGONAL to status: a held order keeps its lifecycle state and is refused at the guards. How far the hold reaches is the tenant&#039;s call (on_hold_blocks: shipping only, shipping and cancellation, or nothing at all).
    organization_id : Optional[str]
        The COMPANY the order is booked on — an organization in the customers app, and the B2B half of who ordered. This is what orders.reports.customer-rollup aggregates by and what makes an order visible to a buyer&#039;s colleagues. Null on a private or guest order, which the rollup counts separately because it cannot attribute it.
    payment : Optional[Dict[str, Any]]
        The payment arrangement as it was chosen, FROZEN. This app reads exactly two keys and stores the rest untouched: &#039;status&#039; seeds payment_status at place-time when it names one of the permitted values (anything else is ignored and the order starts &#039;open&#039;), and &#039;payment_id&#039; is merged in by POST /orders/{id}/payment-status. The method itself, its provider fields and any redirect state belong to the payments app.
    payment_status : Optional[OrderPaymentStatus]
        Whether the order is PAID, and the dimension this app does not decide: it is fed from outside through POST /orders/{id}/payment-status (the payments app or an ERP), and only seeded at place-time from payment.status. Orthogonal to the lifecycle — a completed order can still be open, and a paid one can still be pending.
    placed_at : Optional[str]
        When the order was PLACED. Null while it is pending approval: an order awaiting sign-off exists but was never placed, and that is exactly the difference this field records.
    shipping : Optional[Dict[str, Any]]
        The shipping arrangement as it was chosen, FROZEN. Two keys are READ at place-time and feed the totals: &#039;price&#039; becomes shipping_total (the shipping_total field is only the fallback when this is absent) and &#039;tax_rate&#039; is what shipping is taxed at, because shipping is a Nebenleistung and is taxed too. Everything else — the carrier product, the delivery window, the pickup point — is stored untouched and belongs to the shipping app.
    shipping_address : Optional[Dict[str, Any]]
        The delivery address, FROZEN at place-time — what goes on the label of every shipment of this order. Null on an order that is never delivered (a service, a digital item, a collection).
    shipping_total : Optional[float]
        NET shipping cost, taken from shipping.price or, when the snapshot carries no price, from the request&#039;s shipping_total. In `currency`.
    status : Optional[OrderStatus]
        Where the order stands in its LIFECYCLE, and one of three independent status dimensions. &#039;pending&#039; = created but not placed, an order waiting for approval; &#039;placed&#039; = accepted, nothing shipped; &#039;in_fulfillment&#039; = part of it has gone out, or all of it has and the tenant does not close on shipment; &#039;completed&#039; and &#039;cancelled&#039; end it. Moved by the action routes only — it is not writable through PUT /orders/{id}.
    subtotal : Optional[float]
        NET total of the positions (the sum of their line_total), COMPUTED here at place-time. In `currency`, four decimal places. A caller cannot set it.
    tax_total : Optional[float]
        All tax on this order: the positions&#039; tax_amount plus the tax on shipping (shipping_total × shipping.tax_rate). COMPUTED here — a caller cannot set it.
    updated_at : Optional[str]
        When any column of the order last changed — every status move, every re-derived fulfillment, every modification.
    user_data : Optional[Dict[str, Any]]
        Free-form data belonging to the ORDERING side — carried through from the storefront or the cart and handed back untouched. One of the few fields PUT /orders/{id} may still change.
    """
    acknowledged_at: Optional[str] = Field(default=None, alias='acknowledged_at')
    billing_address: Optional[Dict[str, Any]] = Field(default=None, alias='billing_address')
    buyer: Optional[Dict[str, Any]] = Field(default=None, alias='buyer')
    cancelled_at: Optional[str] = Field(default=None, alias='cancelled_at')
    cart_id: Optional[str] = Field(default=None, alias='cart_id')
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    completed_at: Optional[str] = Field(default=None, alias='completed_at')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    currency: Optional[str] = Field(default=None, alias='currency')
    customer_order_number: Optional[str] = Field(default=None, alias='customer_order_number')
    external_ref: Optional[str] = Field(default=None, alias='external_ref')
    fulfillment_status: Optional[OrderFulfillmentStatus] = Field(default=None, alias='fulfillment_status')
    grand_total: Optional[float] = Field(default=None, alias='grand_total')
    hold_reason: Optional[str] = Field(default=None, alias='hold_reason')
    id: Optional[str] = Field(default=None, alias='id')
    item_count: Optional[float] = Field(default=None, alias='item_count')
    items: Optional[List[OrderItem]] = Field(default=None, alias='items')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    number: Optional[str] = Field(default=None, alias='number')
    on_hold: Optional[bool] = Field(default=None, alias='on_hold')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    payment: Optional[Dict[str, Any]] = Field(default=None, alias='payment')
    payment_status: Optional[OrderPaymentStatus] = Field(default=None, alias='payment_status')
    placed_at: Optional[str] = Field(default=None, alias='placed_at')
    shipping: Optional[Dict[str, Any]] = Field(default=None, alias='shipping')
    shipping_address: Optional[Dict[str, Any]] = Field(default=None, alias='shipping_address')
    shipping_total: Optional[float] = Field(default=None, alias='shipping_total')
    status: Optional[OrderStatus] = Field(default=None, alias='status')
    subtotal: Optional[float] = Field(default=None, alias='subtotal')
    tax_total: Optional[float] = Field(default=None, alias='tax_total')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
    user_data: Optional[Dict[str, Any]] = Field(default=None, alias='user_data')
