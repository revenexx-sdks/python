from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketCloneSeeded(AppwriteModel):
    """
    Rows this call added that were copied from nowhere, because the new market would otherwise have been left unable to trade: the tenant `fallback_locale` when neither market had a locale, and the base currency when it is not in the copied set. Zero on both is the normal, healthy answer — it means nothing had to be invented.

    Attributes
    ----------
    currencies : Optional[float]
        1 when the market&#039;s own base currency was registered because the copied set did not contain it; 0 otherwise.
    locales : Optional[float]
        1 when the tenant&#039;s fallback_locale was written as this market&#039;s only locale, marked default; 0 otherwise.
    """
    currencies: Optional[float] = Field(default=None, alias='currencies')
    locales: Optional[float] = Field(default=None, alias='locales')
