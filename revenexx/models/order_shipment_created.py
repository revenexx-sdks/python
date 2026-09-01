from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .order import Order
from .order_shipment import OrderShipment

class OrderShipmentCreated(AppwriteModel):
    """
    What the booking produced: the new shipment with the quantities it took, and the order as it now stands.

    Attributes
    ----------
    order : Optional[Order]
        The order after the booking: fulfillment_status is re-derived from the positions, and status may have moved to in_fulfillment or (depending on the tenant&#039;s auto_complete_on) completed.
    shipment : Optional[OrderShipment]
        The shipment that was created, WITH the position quantities it booked — the only place a caller learns which quantities actually went out when the positions were defaulted.
    """
    order: Optional[Order] = Field(default=None, alias='order')
    shipment: Optional[OrderShipment] = Field(default=None, alias='shipment')
