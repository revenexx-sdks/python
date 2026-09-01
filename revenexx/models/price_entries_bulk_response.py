from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.price_entries_bulk_mode import PriceEntriesBulkMode

class PriceEntriesBulkResponse(AppwriteModel):
    """
    Counts, not rows: an import chunk of 5000 does not echo 5000 entries back.

    Attributes
    ----------
    created : Optional[float]
        Rows inserted — rungs this list did not have.
    mode : Optional[PriceEntriesBulkMode]
        The mode actually applied — the request&#039;s, or the default `upsert`.
    updated : Optional[float]
        Existing rungs rewritten in place (always 0 in append mode).
    """
    created: Optional[float] = Field(default=None, alias='created')
    mode: Optional[PriceEntriesBulkMode] = Field(default=None, alias='mode')
    updated: Optional[float] = Field(default=None, alias='updated')
