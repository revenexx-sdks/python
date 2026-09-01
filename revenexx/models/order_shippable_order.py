from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_fulfillment_status import OrderFulfillmentStatus
from ..enums.order_status import OrderStatus

class OrderShippableOrder(AppwriteModel):
    """
    Just enough of the order to render the answer — the full row is GET /orders/{id}.

    Attributes
    ----------
    fulfillment_status : Optional[OrderFulfillmentStatus]
        Whether the order has SHIPPED, and the one dimension nobody writes: it is DERIVED after every quantity change from the positions&#039; own bookkeeping. &#039;fulfilled&#039; means shipped &gt;= ordered − cancelled across all positions, &#039;partial&#039; means something went out. Sending it has no effect; ship, cancel or return something and it moves.
    hold_reason : Optional[str]
        Why the order is held, in the words the shipping guard quotes back. Null when it is not held — releasing a hold clears it.
    id : Optional[str]
        The order this answer is about.
    number : Optional[str]
        The order number a human quotes — drawn from the tenant&#039;s order range at place-time, unique per tenant and never reused. It is NOT the id: every route addresses an order by uuid, and GET /orders?number=… is how a number becomes one.
    on_hold : Optional[bool]
        A business stop, ORTHOGONAL to status: a held order keeps its lifecycle state and is refused at the guards. How far the hold reaches is the tenant&#039;s call (on_hold_blocks: shipping only, shipping and cancellation, or nothing at all).
    status : Optional[OrderStatus]
        Where the order stands in its LIFECYCLE, and one of three independent status dimensions. &#039;pending&#039; = created but not placed, an order waiting for approval; &#039;placed&#039; = accepted, nothing shipped; &#039;in_fulfillment&#039; = part of it has gone out, or all of it has and the tenant does not close on shipment; &#039;completed&#039; and &#039;cancelled&#039; end it. Moved by the action routes only — it is not writable through PUT /orders/{id}.
    """
    fulfillment_status: Optional[OrderFulfillmentStatus] = Field(default=None, alias='fulfillment_status')
    hold_reason: Optional[str] = Field(default=None, alias='hold_reason')
    id: Optional[str] = Field(default=None, alias='id')
    number: Optional[str] = Field(default=None, alias='number')
    on_hold: Optional[bool] = Field(default=None, alias='on_hold')
    status: Optional[OrderStatus] = Field(default=None, alias='status')
