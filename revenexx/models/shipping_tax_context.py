from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.shipping_tax_unresolved_reason import ShippingTaxUnresolvedReason
from ..enums.shipping_tax_market_source import ShippingTaxMarketSource
from ..enums.shipping_tax_context_via import ShippingTaxContextVia

class ShippingTaxContext(AppwriteModel):
    """
    Tax resolution status of this answer. resolved=false ⇒ tax_class/tax_rate are unknown, NOT zero.

    Attributes
    ----------
    market_id : Optional[str]
        The market whose tax classes were applied.
    message : Optional[str]
        Human-readable form of `reason`, safe to log or show an operator. One sentence per reason; the example is the `no_markets` wording.
    reason : Optional[ShippingTaxUnresolvedReason]
        Only when resolved=false — why no rate could be applied.
    resolved : Optional[bool]
        Whether a tax rate could be applied at all. FALSE means every rate&#039;s tax_class and tax_rate are UNKNOWN — not zero, and not tax-free. A checkout that adds 0 % on this is wrong; read `reason` and either ask for a market or refuse to quote.
    source : Optional[ShippingTaxMarketSource]
        Where the market came from: &#039;request&#039; (market_id), &#039;header&#039; (x-revenexx-market), &#039;country&#039; (the market matching the destination) or &#039;sole_market&#039; (the tenant has exactly one).
    via : Optional[ShippingTaxContextVia]
        Present when the market is known but registers no tax classes and the tenant&#039;s default_shipping_tax_rate supplied the number instead.
    """
    market_id: Optional[str] = Field(default=None, alias='market_id')
    message: Optional[str] = Field(default=None, alias='message')
    reason: Optional[ShippingTaxUnresolvedReason] = Field(default=None, alias='reason')
    resolved: Optional[bool] = Field(default=None, alias='resolved')
    source: Optional[ShippingTaxMarketSource] = Field(default=None, alias='source')
    via: Optional[ShippingTaxContextVia] = Field(default=None, alias='via')
