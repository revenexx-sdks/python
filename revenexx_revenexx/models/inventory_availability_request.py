from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .inventory_availability_item import InventoryAvailabilityItem

class InventoryAvailabilityRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    items : List[InventoryAvailabilityItem]
        The items to check (batch, at most 200).
    location_code : Optional[str]
        Restrict the check to one location (default: all enabled locations).
    """
    items: List[InventoryAvailabilityItem] = Field(..., alias='items')
    location_code: Optional[str] = Field(default=None, alias='location_code')
