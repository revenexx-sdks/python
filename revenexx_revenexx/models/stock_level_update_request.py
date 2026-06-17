from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class StockLevelUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    location_id : Optional[str]
        Owning location.
    metadata : Optional[Dict[str, Any]]
        Free-form metadata.
    on_hand : Optional[float]
        Physical stock (default 0).
    product_id : Optional[str]
        Tracked product.
    reorder_point : Optional[float]
        Typed model field.
    reserved : Optional[float]
        Reserved stock (default 0) — normally managed by reserve/release/commit.
    sku : Optional[str]
        Tracked SKU (alternative to product_id).
    """
    location_id: Optional[str] = Field(default=None, alias='location_id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    on_hand: Optional[float] = Field(default=None, alias='on_hand')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    reorder_point: Optional[float] = Field(default=None, alias='reorder_point')
    reserved: Optional[float] = Field(default=None, alias='reserved')
    sku: Optional[str] = Field(default=None, alias='sku')
