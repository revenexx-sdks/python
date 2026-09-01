from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .price_entry_replace_item import PriceEntryReplaceItem
from ..enums.price_entries_bulk_mode import PriceEntriesBulkMode

class PriceEntriesBulkRequest(AppwriteModel):
    """
    A chunk of an import. Unlike the replace call it never wipes the list.

    Attributes
    ----------
    entries : List[PriceEntryReplaceItem]
        At most 5000 rows per call — send a large book in chunks.
    mode : Optional[PriceEntriesBulkMode]
        Default &#039;upsert&#039;: a row naming a rung the list already has (same product/sku AND quantity_min) updates it. &#039;append&#039; always inserts — a re-run then duplicates the ladder, which is what makes an ambiguous tier table.
    """
    entries: List[PriceEntryReplaceItem] = Field(..., alias='entries')
    mode: Optional[PriceEntriesBulkMode] = Field(default=None, alias='mode')
