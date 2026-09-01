from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.market_readiness_blocking import MarketReadinessBlocking
from .market_readiness_check import MarketReadinessCheck
from ..enums.market_readiness_warnings import MarketReadinessWarnings

class MarketReadiness(AppwriteModel):
    """
    Can this market actually trade? `ready` is false only when a BLOCKING check failed — no currency to quote in, no tax class to tax with. Warnings are degraded-but-serviceable.

    Attributes
    ----------
    blocking : Optional[List[MarketReadinessBlocking]]
        Ids of the checks that failed BLOCKING — the market cannot do the job at all until each is fixed. Empty exactly when `ready` is true.
    checks : Optional[List[MarketReadinessCheck]]
        Every check that ran, passed or failed, in a fixed order: locales, currencies, tax_classes, tax_basis. `blocking` and `warnings` are the failures from this list by id; this is where the reason lives.
    ready : Optional[bool]
        `blocking` is empty. Deliberately not &quot;every check passed&quot;: a market with one locale and no default flag on it is serviceable, and a verdict that cried wolf about that would be ignored on the day it mattered.
    serving : Optional[bool]
        true when the market&#039;s status is &#039;active&#039;. An active market that is not ready is live and broken — that combination is the one worth an alert.
    warnings : Optional[List[MarketReadinessWarnings]]
        Ids of the checks that failed as WARNINGS — degraded but serviceable, because something else covers for them. A missing locale is only a warning while the tenant declares a fallback_locale.
    """
    blocking: Optional[List[MarketReadinessBlocking]] = Field(default=None, alias='blocking')
    checks: Optional[List[MarketReadinessCheck]] = Field(default=None, alias='checks')
    ready: Optional[bool] = Field(default=None, alias='ready')
    serving: Optional[bool] = Field(default=None, alias='serving')
    warnings: Optional[List[MarketReadinessWarnings]] = Field(default=None, alias='warnings')
