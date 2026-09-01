from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketCurrencyCreateRequest(AppwriteModel):
    """
    The owning market comes from the route path (&#039;market_id&#039;).

    Attributes
    ----------
    code : str
        ISO 4217 code, unique per market — one entry in the set of currencies this market TRADES in, as opposed to the single base currency on the market row that its prices are quoted in. The base currency must appear here or the market cannot serve; clone and backfill register it for you.
    is_default : Optional[bool]
        The currency offered first to a buyer who states no preference. At most one per market, and it should be the market&#039;s base currency — readiness reports it as a warning when it is not.
    position : Optional[float]
        Sort position among this market&#039;s currencies, ascending, default 0 — the order a currency switcher lists them in.
    """
    code: str = Field(..., alias='code')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    position: Optional[float] = Field(default=None, alias='position')
