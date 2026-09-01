from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .price_adjust_preview_row import PriceAdjustPreviewRow
from .price_list_ref import PriceListRef
from ..enums.price_entries_adjust_response_rounding import PriceEntriesAdjustResponseRounding
from ..enums.price_entries_adjust_response_rounding_mode import PriceEntriesAdjustResponseRoundingMode

class PriceEntriesAdjustResponse(AppwriteModel):
    """
    What the change did (or would do, on a dry run), plus the rounding policy it was computed under — so a dialog can show a merchant the before/after before it commits.

    Attributes
    ----------
    dry_run : Optional[bool]
        Echo of the request: true means nothing was written.
    matched : Optional[float]
        Priced entries the filter selected. On-request entries are never counted — a percentage of &quot;ask us&quot; is not a number.
    precision : Optional[float]
        Decimals the new prices were rounded to before snapping — the tenant’s price_precision.
    preview : Optional[List[PriceAdjustPreviewRow]]
        The first 50 changes, before and after. `matched` says how many there were in total.
    preview_truncated : Optional[bool]
        true when more than 50 entries changed, so `preview` is a sample rather than the whole set.
    price_list : Optional[PriceListRef]
        The price list this answer came out of — enough to link to it or to explain the number to a merchant (&quot;this came from the dealer list&quot;).
    rounding : Optional[PriceEntriesAdjustResponseRounding]
        The price ending the results were snapped to — the request’s, or the tenant’s bulk_adjust_rounding where it sent none.
    rounding_mode : Optional[PriceEntriesAdjustResponseRoundingMode]
        How they landed on the last decimal — the tenant’s rounding_mode.
    updated : Optional[float]
        Rows actually written — 0 on a dry run, and a price that came out unchanged is not rewritten.
    """
    dry_run: Optional[bool] = Field(default=None, alias='dry_run')
    matched: Optional[float] = Field(default=None, alias='matched')
    precision: Optional[float] = Field(default=None, alias='precision')
    preview: Optional[List[PriceAdjustPreviewRow]] = Field(default=None, alias='preview')
    preview_truncated: Optional[bool] = Field(default=None, alias='preview_truncated')
    price_list: Optional[PriceListRef] = Field(default=None, alias='price_list')
    rounding: Optional[PriceEntriesAdjustResponseRounding] = Field(default=None, alias='rounding')
    rounding_mode: Optional[PriceEntriesAdjustResponseRoundingMode] = Field(default=None, alias='rounding_mode')
    updated: Optional[float] = Field(default=None, alias='updated')
