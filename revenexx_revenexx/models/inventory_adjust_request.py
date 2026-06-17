from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .inventory_adjust_item import InventoryAdjustItem

class InventoryAdjustRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    items : List[InventoryAdjustItem]
        The corrections — quantities are SIGNED deltas (at most 200).
    location_code : Optional[str]
        Adjusted location (default &#039;main&#039;).
    reason : str
        Mandatory audit reason — every adjustment is a ledger row.
    """
    items: List[InventoryAdjustItem] = Field(..., alias='items')
    location_code: Optional[str] = Field(default=None, alias='location_code')
    reason: str = Field(..., alias='reason')
