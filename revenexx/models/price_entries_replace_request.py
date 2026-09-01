from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .price_entry_replace_item import PriceEntryReplaceItem

class PriceEntriesReplaceRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    entries : List[PriceEntryReplaceItem]
        The complete new entry set (set semantics).
    """
    entries: List[PriceEntryReplaceItem] = Field(..., alias='entries')
