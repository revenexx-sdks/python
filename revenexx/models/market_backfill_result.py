from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .market_backfill_added import MarketBackfillAdded
from .market_backfill_kept import MarketBackfillKept
from .market import Market
from .market_readiness import MarketReadiness
from .market_backfill_seeded import MarketBackfillSeeded
from .market_ref import MarketRef

class MarketBackfillResult(AppwriteModel):
    """
    What the repair changed. `kept` + `added` + `seeded` is what the market now holds, and separating them is the point: it shows that nothing the merchant had already decided was touched.

    Attributes
    ----------
    added : Optional[MarketBackfillAdded]
        Child rows copied in from the source, per collection — only codes this market did not already carry. Zero everywhere on a second run: the call is idempotent.
    kept : Optional[MarketBackfillKept]
        What this market already held BEFORE the repair, per collection — the rows that were left exactly as the merchant left them.
    market : Optional[Market]
        A distinct business context within a tenant — a country, a region, or a storefront segment such as B2C vs B2B — with its own base currency, locales, traded currencies and tax classes. A market is also the platform&#039;s `market` SCOPE dimension: every other commerce app slices its data by one, keyed on this row&#039;s `code`. A market is never just this row: it needs at least one locale, one currency and one tax class before it can serve, which is what /readiness measures and what /clone and /backfill build.
    readiness : Optional[MarketReadiness]
        Can this market actually trade? `ready` is false only when a BLOCKING check failed — no currency to quote in, no tax class to tax with. Warnings are degraded-but-serviceable.
    seeded : Optional[MarketBackfillSeeded]
        Rows this call added that were copied from nowhere, because the new market would otherwise have been left unable to trade: the tenant `fallback_locale` when neither market had a locale, and the base currency when it is not in the copied set. Zero on both is the normal, healthy answer — it means nothing had to be invented.
    source : Optional[MarketRef]
        The market that was read from, resolved — so a caller who passed a code back gets the uuid, and one who passed a uuid gets the code the rest of the platform stores.
    """
    added: Optional[MarketBackfillAdded] = Field(default=None, alias='added')
    kept: Optional[MarketBackfillKept] = Field(default=None, alias='kept')
    market: Optional[Market] = Field(default=None, alias='market')
    readiness: Optional[MarketReadiness] = Field(default=None, alias='readiness')
    seeded: Optional[MarketBackfillSeeded] = Field(default=None, alias='seeded')
    source: Optional[MarketRef] = Field(default=None, alias='source')
