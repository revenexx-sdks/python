from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderShipmentItem(AppwriteModel):
    """
    One line of a delivery note: how much of one order position went out in one shipment.

    Attributes
    ----------
    created_at : Optional[str]
        When the booking was written.
    id : Optional[str]
        Primary key of the booked position line.
    order_item_id : Optional[str]
        Which order position went out. Always a position of the same order as the shipment.
    quantity : Optional[float]
        How much of that position this shipment carried. The sum of these over all shipments is the position&#039;s quantity_shipped.
    shipment_id : Optional[str]
        The shipment this booking belongs to. Deleting the shipment deletes it.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    order_item_id: Optional[str] = Field(default=None, alias='order_item_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    shipment_id: Optional[str] = Field(default=None, alias='shipment_id')
