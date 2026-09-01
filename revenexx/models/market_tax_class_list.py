from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .market_tax_class_filter import MarketTaxClassFilter
from .market_tax_class import MarketTaxClass
from .markets_page import MarketsPage

class MarketTaxClassList(AppwriteModel):
    """
    One page of tax classes of a market, the page it sits on, and the filters that produced it.

    Attributes
    ----------
    filter : Optional[MarketTaxClassFilter]
        The exact-column filters this call applied, echoed back. Every value is the raw query string, never the column&#039;s own type: `?is_default=true` comes back as `&quot;true&quot;`. A `?column=value` naming a column this entity does not have is DROPPED rather than refused — the call answers 200 with the unfiltered list, and the key missing from here is the only way to find out.
    items : Optional[List[MarketTaxClass]]
        The tax classes of a market on this page, in `order` — by `position` ascending unless the call asked otherwise.
    page : Optional[MarketsPage]
        Where in the result set this answer sits. `limit` and `offset` are the values that were APPLIED, not the ones that were asked for — the data plane clamps rather than refuses, so an out-of-range or unparseable value comes back corrected here instead of as a 400.
    """
    filter: Optional[MarketTaxClassFilter] = Field(default=None, alias='filter')
    items: Optional[List[MarketTaxClass]] = Field(default=None, alias='items')
    page: Optional[MarketsPage] = Field(default=None, alias='page')
