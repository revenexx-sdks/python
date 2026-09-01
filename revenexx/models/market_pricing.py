from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.market_pricing_source import MarketPricingSource
from ..enums.market_tax_basis import MarketTaxBasis

class MarketPricing(AppwriteModel):
    """
    Whether a stored price in this market is NET or GROSS — the market layer of an answer the prices app also holds. A price list&#039;s own tax_basis wins over this; `tax_basis: null` with `source: &#039;unset&#039;` means this market declares nothing and the reader must fall through to the tenant&#039;s own default.

    Attributes
    ----------
    prices_include_tax : Optional[bool]
        The raw `prices_include_tax` setting resolved for this market. Null means the market declares nothing — it is NOT a false, and turning it into one is the bug this key exists to prevent.
    source : Optional[MarketPricingSource]
        Where the value came from. &#039;market&#039; — configured on this market. &#039;tenant&#039; — the market holds no value of its own and the tenant baseline answered. &#039;unset&#039; — nothing is configured anywhere in this app, and the reader must fall through to the prices app&#039;s tax_inclusive_default.
    tax_basis : Optional[MarketTaxBasis]
        The same answer in the prices app&#039;s own vocabulary, so the two halves of the platform use one word: &#039;gross&#039; means a stored price already contains tax, &#039;net&#039; means tax is added on top. Null means fall through to the tenant&#039;s own default.
    """
    prices_include_tax: Optional[bool] = Field(default=None, alias='prices_include_tax')
    source: Optional[MarketPricingSource] = Field(default=None, alias='source')
    tax_basis: Optional[MarketTaxBasis] = Field(default=None, alias='tax_basis')
