from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .order_shipment_item import OrderShipmentItem

class OrderShipment(AppwriteModel):
    """
    One handover to a carrier — a delivery note. An order has as many of these as it took to get the goods out; each carries the position quantities it booked.

    Attributes
    ----------
    carrier : Optional[str]
        Who is carrying it, in the merchant&#039;s own words. Free text — this app neither validates it nor knows the carrier&#039;s API.
    created_at : Optional[str]
        When the shipment was booked here, which is not necessarily when it left — that is shipped_at.
    id : Optional[str]
        Primary key of the shipment.
    items : Optional[List[OrderShipmentItem]]
        The booked position quantities of this shipment.
    metadata : Optional[Dict[str, Any]]
        Free-form data for the caller — the warehouse system&#039;s own reference for this handover. Stored and returned untouched.
    number : Optional[str]
        The DELIVERY NOTE number — drawn from the tenant&#039;s delivery range, unique per tenant, and a different series from the order number. A caller may supply its own when the number is issued by the warehouse system instead.
    order_id : Optional[str]
        The order this shipment belongs to. Deleting the order deletes its shipments.
    shipped_at : Optional[str]
        When the goods actually left. Defaults to now, and a caller may backdate it — a shipment booked on Monday for a Friday handover says Friday.
    tracking_code : Optional[str]
        The consignment number the carrier issued. Free text: every carrier formats it differently and this app stores whatever it is given.
    tracking_url : Optional[str]
        Where a human can follow the parcel. Supplied by the caller — this app does not build it, because only the caller knows the carrier&#039;s tracking address.
    """
    carrier: Optional[str] = Field(default=None, alias='carrier')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    items: Optional[List[OrderShipmentItem]] = Field(default=None, alias='items')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    number: Optional[str] = Field(default=None, alias='number')
    order_id: Optional[str] = Field(default=None, alias='order_id')
    shipped_at: Optional[str] = Field(default=None, alias='shipped_at')
    tracking_code: Optional[str] = Field(default=None, alias='tracking_code')
    tracking_url: Optional[str] = Field(default=None, alias='tracking_url')
