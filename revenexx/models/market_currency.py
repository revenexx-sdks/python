from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketCurrency(AppwriteModel):
    """
    One currency a market accepts, as opposed to the single base currency on the market row that its prices are quoted in. The base currency must be registered here or the market cannot serve.

    Attributes
    ----------
    code : Optional[str]
        ISO 4217 code, unique per market — one entry in the set of currencies this market TRADES in, as opposed to the single base currency on the market row that its prices are quoted in. The base currency must appear here or the market cannot serve; clone and backfill register it for you.
    created_at : Optional[str]
        When the currency was registered on this market. Set by the database; never writable.
    id : Optional[str]
        Primary key of this currency registration. The currency is named by `code` everywhere else.
    is_default : Optional[bool]
        The currency offered first to a buyer who states no preference. At most one per market, and it should be the market&#039;s base currency — readiness reports it as a warning when it is not.
    market_id : Optional[str]
        The market this currency belongs to. Filled from the route path on write and never read out of the body; ON DELETE CASCADE, so deleting the market deletes this row.
    position : Optional[float]
        Sort position among this market&#039;s currencies, ascending, default 0 — the order a currency switcher lists them in.
    """
    code: Optional[str] = Field(default=None, alias='code')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    market_id: Optional[str] = Field(default=None, alias='market_id')
    position: Optional[float] = Field(default=None, alias='position')
