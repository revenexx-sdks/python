from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .order_shipment_position import OrderShipmentPosition

class OrderShipmentCreateRequest(AppwriteModel):
    """
    Create a shipment. Omitted positions = ship everything still open.

    Attributes
    ----------
    carrier : Optional[str]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Free-form metadata.
    number : Optional[str]
        Delivery note number — drawn from the &#039;delivery&#039; range when omitted.
    positions : Optional[List[OrderShipmentPosition]]
        Omitted = every position with open quantity, in full.
    shipped_at : Optional[str]
        Defaults to now.
    tracking_code : Optional[str]
        Typed model field.
    tracking_url : Optional[str]
        Typed model field.
    """
    carrier: Optional[str] = Field(default=None, alias='carrier')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    number: Optional[str] = Field(default=None, alias='number')
    positions: Optional[List[OrderShipmentPosition]] = Field(default=None, alias='positions')
    shipped_at: Optional[str] = Field(default=None, alias='shipped_at')
    tracking_code: Optional[str] = Field(default=None, alias='tracking_code')
    tracking_url: Optional[str] = Field(default=None, alias='tracking_url')
