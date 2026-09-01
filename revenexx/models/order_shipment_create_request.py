from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .order_shipment_position import OrderShipmentPosition

class OrderShipmentCreateRequest(AppwriteModel):
    """
    Book what went out. Every field is optional: an empty body ships every position that still has an open quantity, in full, on a delivery note number drawn from the tenant&#039;s delivery range — which is the whole payload for the common case.

    Attributes
    ----------
    carrier : Optional[str]
        Who is carrying it, in the merchant&#039;s own words. Free text — this app neither validates it nor knows the carrier&#039;s API.
    metadata : Optional[Dict[str, Any]]
        Free-form data for the caller — the warehouse system&#039;s own reference for this handover. Stored and returned untouched.
    number : Optional[str]
        The DELIVERY NOTE number — drawn from the tenant&#039;s delivery range, unique per tenant, and a different series from the order number. A caller may supply its own when the number is issued by the warehouse system instead. Drawn from the &#039;delivery&#039; range when omitted; supply one only when the number is issued elsewhere.
    positions : Optional[List[OrderShipmentPosition]]
        What this shipment carries. Omitted = every position with an open quantity, in full. GET /orders/{id}/shippable answers exactly the budget each one is guarded against.
    shipped_at : Optional[str]
        When the goods actually left. Defaults to now, and a caller may backdate it — a shipment booked on Monday for a Friday handover says Friday.
    tracking_code : Optional[str]
        The consignment number the carrier issued. Free text: every carrier formats it differently and this app stores whatever it is given.
    tracking_url : Optional[str]
        Where a human can follow the parcel. Supplied by the caller — this app does not build it, because only the caller knows the carrier&#039;s tracking address.
    """
    carrier: Optional[str] = Field(default=None, alias='carrier')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    number: Optional[str] = Field(default=None, alias='number')
    positions: Optional[List[OrderShipmentPosition]] = Field(default=None, alias='positions')
    shipped_at: Optional[str] = Field(default=None, alias='shipped_at')
    tracking_code: Optional[str] = Field(default=None, alias='tracking_code')
    tracking_url: Optional[str] = Field(default=None, alias='tracking_url')
