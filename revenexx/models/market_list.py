from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .market_filter import MarketFilter
from .market import Market
from .markets_page import MarketsPage

class MarketList(AppwriteModel):
    """
    One page of markets, the page it sits on, and the filters that produced it.

    Attributes
    ----------
    filter : Optional[MarketFilter]
        The exact-column filters this call applied, echoed back. Every value is the raw query string, never the column&#039;s own type: `?is_default=true` comes back as `&quot;true&quot;`. A `?column=value` naming a column this entity does not have is DROPPED rather than refused — the call answers 200 with the unfiltered list, and the key missing from here is the only way to find out.
    items : Optional[List[Market]]
        The markets on this page, in `order` — by `position` ascending unless the call asked otherwise.
    page : Optional[MarketsPage]
        Where in the result set this answer sits. `limit` and `offset` are the values that were APPLIED, not the ones that were asked for — the data plane clamps rather than refuses, so an out-of-range or unparseable value comes back corrected here instead of as a 400.
    """
    filter: Optional[MarketFilter] = Field(default=None, alias='filter')
    items: Optional[List[Market]] = Field(default=None, alias='items')
    page: Optional[MarketsPage] = Field(default=None, alias='page')
