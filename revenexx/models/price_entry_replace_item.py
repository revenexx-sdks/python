from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.price_entry_type import PriceEntryType

class PriceEntryReplaceItem(AppwriteModel):
    """
    An entry needs an identity: &#039;product_id&#039; or &#039;sku&#039; — every other field is normalized to its default when null/omitted.

    Attributes
    ----------
    metadata : Optional[Dict[str, Any]]
        Free-form bag: whatever JSON object you write round-trips exactly, and this app never reads it. Its keys are yours.
    price_type : Optional[PriceEntryType]
        Default &#039;standard&#039;; &#039;on_request&#039; is the explicit no-price marker — it STOPS resolution for this item on this list and answers &quot;price on request&quot; even where a cheaper list exists.
    product_id : Optional[str]
        The product this rung prices. An entry needs product_id or sku — the row CHECK enforces it.
    quantity_min : Optional[float]
        Tier threshold (Staffelpreis): this price applies from this quantity upwards (default 1). The rungs of one item are the entries sharing its identity; the highest threshold at or below the requested quantity wins.
    sku : Optional[str]
        The article number this rung prices (alternative to product_id). Matched exactly on resolve — never normalised or case-folded.
    unit : Optional[str]
        Unit of measure the price is per — free text, neither validated nor converted here. A resolve call’s `quantity` is counted in it.
    unit_price : Optional[float]
        Price for ONE unit of `unit`, in the LIST’s currency and on the LIST’s tax basis — a decimal amount in major units (19.90), never minor units/cents. Stored at 4 decimals and echoed back exactly as sent (default 0).
    valid_from : Optional[str]
        Start of this entry’s own validity (ISO 8601) — how a promo price is expressed: a second rung, live only for its window. null = open-ended.
    valid_until : Optional[str]
        End of this entry’s own validity; null = open-ended. Outside it the rung is skipped and the ladder resolves as if it were not there.
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
