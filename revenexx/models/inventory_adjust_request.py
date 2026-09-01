from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .inventory_adjust_item import InventoryAdjustItem

class InventoryAdjustRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    items : Optional[List[InventoryAdjustItem]]
        The corrections, at most 200 in one call — a stocktake, breakage, shrinkage. Quantities are SIGNED deltas, not new balances.
    location_code : Optional[str]
        Which location is being corrected. Omitted, the `default_location_code` setting decides. A correction is per location: the same SKU in two warehouses is two corrections.
    product_id : Optional[str]
        Inline single-item form: the product to move, instead of a one-entry `items` array. The two forms are equivalent — nothing downstream knows which arrived.
    quantity : Optional[float]
        Inline single-item form: the SIGNED correction (negative writes stock off, positive finds it). Non-zero.
    reason : Optional[str]
        Why the stock is being corrected — this is the audit trail a stocktake leaves behind. Owed unless `movement_reason_required` is &#039;none&#039; (its default, &#039;adjustments&#039;, asks for one exactly here); missing where it is owed, the call is 400.
    sku : Optional[str]
        Inline single-item form: the article number to move (instead of `product_id`).
    """
    items: Optional[List[InventoryAdjustItem]] = Field(default=None, alias='items')
    location_code: Optional[str] = Field(default=None, alias='location_code')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    reason: Optional[str] = Field(default=None, alias='reason')
    sku: Optional[str] = Field(default=None, alias='sku')
