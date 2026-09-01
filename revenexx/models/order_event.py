from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderEvent(AppwriteModel):
    """
    One entry of the audit trail, which is also the domain event feed: every action writes a row, the manifest emits order_event.created on insert, and the row name IS the event name on the bus.

    Attributes
    ----------
    actor : Optional[str]
        Who caused it: the resolved contact id of the acting principal. Only order.placed and order.requested carry one today — every other row is null — so filtering on it filters to those two names. The database constrains nothing here (the column is text); the uuid shape is what this app WRITES, which is also why no example is published: no id an app invents names a row a tenant holds.
    created_at : Optional[str]
        When it happened. The trail comes back oldest first, which is the order a human reads a history in.
    id : Optional[str]
        Primary key of the event row.
    name : Optional[str]
        WHAT happened, and this is the domain event: the manifest emits order_event.created on insert and this value is the event name on the bus. The names this app writes are order.placed, order.requested, order.updated, order.acknowledged, order.cancelled, order.item.cancelled, order.shipment.created, order.completed, order.held, order.unheld, order.payment_status.changed, order.comment.added, order.return.registered, order.return.received, order.return.completed and order.return.rejected.
    order_id : Optional[str]
        The order this happened to.
    payload : Optional[Dict[str, Any]]
        The machine-readable body, and its shape follows `name`. order.placed / order.requested carry number, grand_total, currency, item_count, cart_id — plus approval_reason (permission | value_threshold) and threshold when the order is waiting for sign-off. order.shipment.created carries shipment_id, number, carrier, tracking_code and the booked positions. order.item.cancelled and order.return.* carry positions and the reason or resolution. order.completed carries via (shipment | payment | manual). order.payment_status.changed carries from, to and payment_id. Nothing validates it: it is what the route that wrote the row put there.
    """
    actor: Optional[str] = Field(default=None, alias='actor')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    name: Optional[str] = Field(default=None, alias='name')
    order_id: Optional[str] = Field(default=None, alias='order_id')
    payload: Optional[Dict[str, Any]] = Field(default=None, alias='payload')
