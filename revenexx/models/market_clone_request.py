from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.market_status import MarketStatus

class MarketCloneRequest(AppwriteModel):
    """
    The path id is the SOURCE market (a uuid or a market code). Everything the new market does not inherit is here. The copy flags default to true; `is_default` is never copied, and the new market always gets its own base currency registered and marked default.

    Attributes
    ----------
    code : str
        Code of the NEW market (unique per tenant).
    copy_currencies : Optional[bool]
        Copy the source&#039;s traded currencies. Default true. The new market&#039;s own base currency is registered and marked default either way.
    copy_locales : Optional[bool]
        Copy the source&#039;s locales. Default true. False leaves the new market with no language of its own, so the tenant fallback_locale is seeded instead — it is never left with none.
    copy_tax_classes : Optional[bool]
        Copy the source&#039;s tax classes, rates and all. Default true. False leaves the market unable to tax anything, which readiness reports as blocking.
    currency : Optional[str]
        Base currency of the new market (ISO 4217). Defaults to the source market&#039;s, and is registered and marked default on the new one either way.
    name : Optional[str]
        Display name of the new market. Defaults to its code.
    status : Optional[MarketStatus]
        Status of the new market. Defaults to &#039;active&#039;; clone it &#039;inactive&#039; to build it out before it serves anyone.
    """
    code: str = Field(..., alias='code')
    copy_currencies: Optional[bool] = Field(default=None, alias='copy_currencies')
    copy_locales: Optional[bool] = Field(default=None, alias='copy_locales')
    copy_tax_classes: Optional[bool] = Field(default=None, alias='copy_tax_classes')
    currency: Optional[str] = Field(default=None, alias='currency')
    name: Optional[str] = Field(default=None, alias='name')
    status: Optional[MarketStatus] = Field(default=None, alias='status')
