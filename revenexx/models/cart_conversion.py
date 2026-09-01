from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .cart_conversion_pricing import CartConversionPricing
from .cart_conversion_reservation import CartConversionReservation
from ..enums.cart_status import CartStatus

class CartConversion(AppwriteModel):
    """
    

    Attributes
    ----------
    abandoned_at : Optional[str]
        When the cart was abandoned — by hand, or by the cart-maintenance sweep. This is the only instant the abandonment funnel has, and nothing else in the platform writes it. carts.reopen clears it.
    channel_id : Optional[str]
        The sales channel the cart was opened in (web shop, app, agent desk), as a channel of the channels app. Carried to the order for attribution; nothing in this app reads it.
    contact_id : Optional[str]
        The customer who owns this cart, as a contact of the customers app. Null on a guest cart: the database requires one of contact_id and session_key, never neither.
    created_at : Optional[str]
        When the cart was opened.
    currency : Optional[str]
        ISO 4217 code the whole cart is priced in. A line added without a currency of its own inherits this one.
    id : Optional[str]
        The cart, as every other route addresses it. Stable for the cart&#039;s whole life: a merge closes a cart, it never renumbers one.
    is_current : Optional[bool]
        THE current cart of this owner — the flag carts.activate writes, and reading it back is what `?is_current=true` is for. At most one cart per owner carries it: activating one clears it on every sibling, and abandoning, ordering or merging a cart clears it. A storefront resuming a session asks for it together with contact_id or session_key.
    item_count : Optional[float]
        Total QUANTITY in the cart, not the number of lines: the sum of every line&#039;s quantity, rounded. Two lines of five pieces each answer 10, not 2. Recomputed by this app after every line write — a value a client sends is ignored.
    market_id : Optional[str]
        The market this cart is scoped to, stamped by the platform. It decides which market&#039;s settings apply — including the retention windows the sweep deletes on. Null on a cart that belongs to no market, which runs on the tenant baseline. Cart lines and io profiles carry no market of their own; a line&#039;s market is its cart&#039;s.
    merged_into_cart_id : Optional[str]
        The cart this one was merged into, written together with status &#039;merged&#039;. The lines are in the target now and this is the trail back — the answer to &#039;where did my cart go&#039;. Null on every cart that was never merged.
    metadata : Optional[Dict[str, Any]]
        Free-form data the storefront hangs on the cart. Stored and returned verbatim; no key in here is read by this app, and none is indexed.
    name : Optional[str]
        What the buyer calls this cart. B2B customers keep several named carts side by side — &#039;Weekly order&#039;, &#039;Site B&#039;, &#039;Q3 budget&#039; — which is what multi_cart_enabled turns on; a storefront with one cart per buyer leaves it at the default &#039;Cart&#039;.
    order_ref : Optional[str]
        The order this cart became, in whatever numbering order management uses. Free text: this app stores what it is handed and never resolves it. Filtering on it is how a support agent gets from an order number back to the cart behind it.
    ordered_at : Optional[str]
        When the cart was handed to order management. Written once, with the status, and never cleared.
    pricing : Optional[CartConversionPricing]
        How price_snapshot_mode settled the two prices every line carries.
    reservation : Optional[CartConversionReservation]
        What this app ASKED inventories for, and what it answered. This app holds no stock: inventories picks the location, applies the backorder policy and owns the hold&#039;s expiry.
    session_key : Optional[str]
        How a cart is identified BEFORE anyone logs in — the opaque key the storefront already keeps in its own session or cookie and sends back on every anonymous call. This app neither issues nor parses it; any non-empty string is a valid key, so its format is the storefront&#039;s own. On login carts.claim hands every active cart of one session_key to a contact, and this becomes null.
    status : Optional[CartStatus]
        Where the cart stands in its lifecycle. &#039;active&#039; is the only status that accepts a write of any kind. &#039;abandoned&#039; is set by hand or by the cart-maintenance sweep and is the one reversible ending (carts.reopen). &#039;ordered&#039; and &#039;merged&#039; are final — the cart is a record now, not a workspace.
    subtotal : Optional[float]
        Sum of every line&#039;s line_total, in the cart&#039;s currency, net — before shipping, before tax. Recomputed after every line write, and written once more by carts.order when price_snapshot_mode settles which of a line&#039;s two prices is charged.
    tenant_id : Optional[str]
        The tenant this row belongs to, echoed by the data plane. Always the tenant the request was made for — it is not a way to reach another one.
    updated_at : Optional[str]
        The last time anything about this cart or its lines changed — every write path in this app stamps it. It is also what the maintenance sweep measures idleness with, which is why the abandonment sweep is the one write that deliberately does not touch it: noticing that a cart is idle must not reset the clock that decides how long it is kept.
    """
    abandoned_at: Optional[str] = Field(default=None, alias='abandoned_at')
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    currency: Optional[str] = Field(default=None, alias='currency')
    id: Optional[str] = Field(default=None, alias='id')
    is_current: Optional[bool] = Field(default=None, alias='is_current')
    item_count: Optional[float] = Field(default=None, alias='item_count')
    market_id: Optional[str] = Field(default=None, alias='market_id')
    merged_into_cart_id: Optional[str] = Field(default=None, alias='merged_into_cart_id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    order_ref: Optional[str] = Field(default=None, alias='order_ref')
    ordered_at: Optional[str] = Field(default=None, alias='ordered_at')
    pricing: Optional[CartConversionPricing] = Field(default=None, alias='pricing')
    reservation: Optional[CartConversionReservation] = Field(default=None, alias='reservation')
    session_key: Optional[str] = Field(default=None, alias='session_key')
    status: Optional[CartStatus] = Field(default=None, alias='status')
    subtotal: Optional[float] = Field(default=None, alias='subtotal')
    tenant_id: Optional[str] = Field(default=None, alias='tenant_id')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
