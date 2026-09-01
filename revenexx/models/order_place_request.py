from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .order_item_create_request import OrderItemCreateRequest

class OrderPlaceRequest(AppwriteModel):
    """
    The snapshot payload: items plus frozen buyer/addresses/payment/shipping. The order number is drawn from the order range, totals are computed from the items.

    Attributes
    ----------
    billing_address : Optional[Dict[str, Any]]
        The invoice address, FROZEN at place-time. Changing the customer&#039;s address afterwards does not change what this order was billed to.
    buyer : Optional[Dict[str, Any]]
        The ordering party as it was at place-time, FROZEN: a copy, not a reference, so the order still reads correctly after the customer record is renamed, merged or deleted. The caller decides what goes in; this app stores it and reads nothing out of it.
    cart_id : Optional[str]
        The cart this order was placed from, when a storefront handed one over. A reference across an app boundary (the carts app), not a foreign key — nothing here checks that it resolves. Null for an order an integration or an operator created. The carts.order hand-over sets it.
    channel_id : Optional[str]
        The sales channel the order arrived through — webshop, app, phone desk, EDI. Null when the caller named none.
    contact_id : Optional[str]
        The PERSON who ordered — a contact in the customers app. Resolved from the acting principal whenever the caller carries one, and a body value that disagrees is refused rather than silently overridden. Null for a guest checkout. Ignored when the caller carries a principal — the RESOLVED contact wins, and a body value that disagrees is a 400 rather than a silent override.
    currency : Optional[str]
        ISO 4217 code of EVERY amount on this order. Frozen at place-time from the market&#039;s default_currency unless the caller named one. Nothing on this order is ever converted, and the approval threshold is read in this currency — which is why the threshold is a per-market setting. Defaults to the market&#039;s default_currency setting.
    customer_order_number : Optional[str]
        The BUYER&#039;s own reference — their purchase-order number. Free text, not unique, never generated here: it exists so the paperwork can carry the number the buyer&#039;s accounts payable will look for. One of the few fields PUT /orders/{id} may still change.
    grand_total : Optional[float]
        Optional, and CHECKED rather than used: the order always computes its own total from the positions, the shipping cost and the tax. Send it as a checksum on that arithmetic — if it agrees the order is placed, and if it disagrees the call is refused with 400 naming both numbers, yours and the computed one. The comparison is at 2 decimal places (this app stores 4, ERPs work to 2, so a difference below a cent is agreement). It is never taken as the order value: the approval threshold and the revenue rollup read the computed number, which is why a total that disagrees is an error rather than an override.
    items : List[OrderItemCreateRequest]
        The order positions — at least one, and at most the tenant&#039;s max_items_per_order (500 out of the box; a longer list is a 400 naming the limit).
    metadata : Optional[Dict[str, Any]]
        Free-form data belonging to the INTEGRATION side — an ERP&#039;s own bookkeeping about this order. Stored and returned untouched; nothing here reads it.
    organization_id : Optional[str]
        The COMPANY the order is booked on — an organization in the customers app, and the B2B half of who ordered. This is what orders.reports.customer-rollup aggregates by and what makes an order visible to a buyer&#039;s colleagues. Null on a private or guest order, which the rollup counts separately because it cannot attribute it. A principal&#039;s own organization wins over this when it has one.
    payment : Optional[Dict[str, Any]]
        The payment arrangement as it was chosen, FROZEN. This app reads exactly two keys and stores the rest untouched: &#039;status&#039; seeds payment_status at place-time when it names one of the permitted values (anything else is ignored and the order starts &#039;open&#039;), and &#039;payment_id&#039; is merged in by POST /orders/{id}/payment-status. The method itself, its provider fields and any redirect state belong to the payments app.
    shipping : Optional[Dict[str, Any]]
        The shipping arrangement as it was chosen, FROZEN. Two keys are READ at place-time and feed the totals: &#039;price&#039; becomes shipping_total (the shipping_total field is only the fallback when this is absent) and &#039;tax_rate&#039; is what shipping is taxed at, because shipping is a Nebenleistung and is taxed too. Everything else — the carrier product, the delivery window, the pickup point — is stored untouched and belongs to the shipping app.
    shipping_address : Optional[Dict[str, Any]]
        The delivery address, FROZEN at place-time — what goes on the label of every shipment of this order. Null on an order that is never delivered (a service, a digital item, a collection).
    shipping_total : Optional[float]
        NET shipping cost, taken from shipping.price or, when the snapshot carries no price, from the request&#039;s shipping_total. In `currency`. Only read when the shipping snapshot carries no &#039;price&#039;.
    user_data : Optional[Dict[str, Any]]
        Free-form data belonging to the ORDERING side — carried through from the storefront or the cart and handed back untouched. One of the few fields PUT /orders/{id} may still change.
    """
    billing_address: Optional[Dict[str, Any]] = Field(default=None, alias='billing_address')
    buyer: Optional[Dict[str, Any]] = Field(default=None, alias='buyer')
    cart_id: Optional[str] = Field(default=None, alias='cart_id')
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    currency: Optional[str] = Field(default=None, alias='currency')
    customer_order_number: Optional[str] = Field(default=None, alias='customer_order_number')
    grand_total: Optional[float] = Field(default=None, alias='grand_total')
    items: List[OrderItemCreateRequest] = Field(..., alias='items')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    payment: Optional[Dict[str, Any]] = Field(default=None, alias='payment')
    shipping: Optional[Dict[str, Any]] = Field(default=None, alias='shipping')
    shipping_address: Optional[Dict[str, Any]] = Field(default=None, alias='shipping_address')
    shipping_total: Optional[float] = Field(default=None, alias='shipping_total')
    user_data: Optional[Dict[str, Any]] = Field(default=None, alias='user_data')
