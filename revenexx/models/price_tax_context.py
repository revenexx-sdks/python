from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.price_tax_unresolved_reason import PriceTaxUnresolvedReason
from ..enums.price_tax_market_source import PriceTaxMarketSource

class PriceTaxContext(AppwriteModel):
    """
    Tax resolution status of this answer. resolved=false ⇒ tax_class/tax_rate are unknown, NOT zero.

    Attributes
    ----------
    market_id : Optional[str]
        The market whose tax classes were applied.
    message : Optional[str]
        Human-readable form of `reason`, in English. Safe to log; not phrased for a buyer.
    reason : Optional[PriceTaxUnresolvedReason]
        Only when resolved=false — why no rate could be applied.
    resolved : Optional[bool]
        true ⇒ every priced item carries `tax_class`, `tax_rate`, `unit_price_net` and `unit_price_gross`. false ⇒ those are null because the rate could not be established — read `reason`, and never as &quot;no tax due&quot;.
    source : Optional[PriceTaxMarketSource]
        Where the market came from: &#039;request&#039; (market_id), &#039;header&#039; (x-revenexx-market) or &#039;sole_market&#039; (the tenant has exactly one).
    """
    market_id: Optional[str] = Field(default=None, alias='market_id')
    message: Optional[str] = Field(default=None, alias='message')
    reason: Optional[PriceTaxUnresolvedReason] = Field(default=None, alias='reason')
    resolved: Optional[bool] = Field(default=None, alias='resolved')
    source: Optional[PriceTaxMarketSource] = Field(default=None, alias='source')
