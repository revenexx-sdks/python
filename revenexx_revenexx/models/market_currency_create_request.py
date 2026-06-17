from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketCurrencyCreateRequest(AppwriteModel):
    """
    The owning market comes from the route path (&#039;market_id&#039;).

    Attributes
    ----------
    code : str
        ISO 4217 code, e.g. EUR (unique per market).
    is_default : Optional[bool]
        Typed model field.
    position : Optional[float]
        Sort position (default 0).
    """
    code: str = Field(..., alias='code')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    position: Optional[float] = Field(default=None, alias='position')
