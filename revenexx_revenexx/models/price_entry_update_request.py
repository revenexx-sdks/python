from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.price_entry_type import PriceEntryType

class PriceEntryUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    metadata : Optional[Dict[str, Any]]
        Free-form metadata.
    price_type : Optional[PriceEntryType]
        Default &#039;standard&#039;; &#039;on_request&#039; is the explicit no-price marker — it stops resolution and answers &quot;price on request&quot;.
    product_id : Optional[str]
        Priced product.
    quantity_min : Optional[float]
        Tier threshold (Staffelpreis): this price applies from this quantity (default 1).
    sku : Optional[str]
        Priced SKU (alternative to product_id).
    unit : Optional[str]
        Typed model field.
    unit_price : Optional[float]
        Per-unit price (default 0).
    valid_from : Optional[str]
        Per-entry validity start (promo prices).
    valid_until : Optional[str]
        Per-entry validity end.
    """
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    price_type: Optional[PriceEntryType] = Field(default=None, alias='price_type')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity_min: Optional[float] = Field(default=None, alias='quantity_min')
    sku: Optional[str] = Field(default=None, alias='sku')
    unit: Optional[str] = Field(default=None, alias='unit')
    unit_price: Optional[float] = Field(default=None, alias='unit_price')
    valid_from: Optional[str] = Field(default=None, alias='valid_from')
    valid_until: Optional[str] = Field(default=None, alias='valid_until')
