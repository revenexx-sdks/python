from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CartAbandonSweep(AppwriteModel):
    """
    The first sweep: active carts nobody has touched since their market&#039;s window become abandoned. Nothing else in the platform ever stamps abandoned_at, so without this the abandonment funnel is empty by construction rather than empty because nobody abandons carts.

    Attributes
    ----------
    abandoned : Optional[float]
        Carts actually marked. 0 on a dry run — see `found`.
    after_minutes : Optional[float]
        The abandon_after_minutes of the TENANT baseline — what a cart in no market ran on. 0 disables the sweep. Carts in a market were each held against their own market&#039;s window, which may differ from this.
    capped : Optional[bool]
        This pass looked at as many carts as one pass looks at, so there may be more behind them. The rest go on the next tick, oldest first — a backlog is visible here rather than merely slow.
    cart_ids : Optional[List[Any]]
        The carts this sweep touched, so a merchant can look at them before or after.
    cutoff : Optional[str]
        Carts untouched since this instant were swept — the BASELINE cutoff. A run no longer has one cutoff, because each cart was held against its own market&#039;s clock; this is the one unassigned carts ran on.
    enabled : Optional[bool]
        At least one window in force (the baseline, or some market&#039;s). False means every applicable window was 0 and nothing was even considered.
    found : Optional[float]
        Carts past their window. On a dry run this is the whole answer — `abandoned` stays 0.
    markets : Optional[List[Any]]
        The market codes this pass came across, so an operator can see whose windows were actually in play. Empty when no examined cart belongs to a market.
    """
    abandoned: Optional[float] = Field(default=None, alias='abandoned')
    after_minutes: Optional[float] = Field(default=None, alias='after_minutes')
    capped: Optional[bool] = Field(default=None, alias='capped')
    cart_ids: Optional[List[Any]] = Field(default=None, alias='cart_ids')
    cutoff: Optional[str] = Field(default=None, alias='cutoff')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    found: Optional[float] = Field(default=None, alias='found')
    markets: Optional[List[Any]] = Field(default=None, alias='markets')
