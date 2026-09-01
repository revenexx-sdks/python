from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ReservationSweepResult(AppwriteModel):
    """
    

    Attributes
    ----------
    expired : Optional[float]
        How many active reservations were found past their hold: the ones with an `expires_at` in the past, plus the undated ones older than their market&#039;s TTL.
    markets : Optional[List[Any]]
        The market codes this run had to resolve a window for — every market that had an undated active reservation. Empty when nothing is market-assigned, which is the usual case.
    released : Optional[float]
        How many were actually given back — `reserved` lowered on the stock row and a `release` booking written for each. It equals `expired` unless a row vanished mid-run. Idempotent: a second run immediately after finds nothing and answers 0.
    swept_at : Optional[str]
        The cut-off this run used — everything whose hold had run out by this moment was released. It is the run&#039;s own clock, not a stored value.
    ttl_minutes : Optional[float]
        The `reservation_ttl_minutes` that applied to reservations belonging to NO market — the tenant baseline. A reservation assigned to a market is judged against that market&#039;s own window instead, which is why this is reported rather than assumed to be the only one.
    """
    expired: Optional[float] = Field(default=None, alias='expired')
    markets: Optional[List[Any]] = Field(default=None, alias='markets')
    released: Optional[float] = Field(default=None, alias='released')
    swept_at: Optional[str] = Field(default=None, alias='swept_at')
    ttl_minutes: Optional[float] = Field(default=None, alias='ttl_minutes')
