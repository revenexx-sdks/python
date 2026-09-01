from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.market_readiness_check_id import MarketReadinessCheckId
from ..enums.market_readiness_severity import MarketReadinessSeverity

class MarketReadinessCheck(AppwriteModel):
    """
    One question asked of the market, its verdict, and how much the answer costs.

    Attributes
    ----------
    detail : Optional[str]
        One sentence naming what was found and, for a warning, what covers for it.
    id : Optional[MarketReadinessCheckId]
        Which question. &#039;locales&#039; — is there a language to render in? &#039;currencies&#039; — is the base currency registered and marked default? &#039;tax_classes&#039; — is there a rate to tax with? &#039;tax_basis&#039; — informational, restating whether stored prices are gross or net.
    ok : Optional[bool]
        Whether this check passed. A false with severity `info` cannot occur — the informational check always passes.
    severity : Optional[MarketReadinessSeverity]
        What a failure costs. &#039;blocking&#039; — the market cannot trade. &#039;warning&#039; — degraded but serviceable, and `detail` names what covers for it. &#039;info&#039; — a fact worth reporting that is never a failure. The severity is not fixed per check: no locales is blocking without a tenant fallback_locale and a warning with one.
    """
    detail: Optional[str] = Field(default=None, alias='detail')
    id: Optional[MarketReadinessCheckId] = Field(default=None, alias='id')
    ok: Optional[bool] = Field(default=None, alias='ok')
    severity: Optional[MarketReadinessSeverity] = Field(default=None, alias='severity')
