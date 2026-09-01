from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .market import Market

class MarketMakeDefaultResponse(AppwriteModel):
    """
    The market as it now stands, plus what had to move out of its way.

    Attributes
    ----------
    demoted : Optional[List[Any]]
        Codes of the markets that lost the flag. Empty when this market already held it — the call is idempotent and writes nothing on a repeat, so an empty array is a success, not a no-op that failed.
    market : Optional[Market]
        A distinct business context within a tenant — a country, a region, or a storefront segment such as B2C vs B2B — with its own base currency, locales, traded currencies and tax classes. A market is also the platform&#039;s `market` SCOPE dimension: every other commerce app slices its data by one, keyed on this row&#039;s `code`. A market is never just this row: it needs at least one locale, one currency and one tax class before it can serve, which is what /readiness measures and what /clone and /backfill build.
    """
    demoted: Optional[List[Any]] = Field(default=None, alias='demoted')
    market: Optional[Market] = Field(default=None, alias='market')
