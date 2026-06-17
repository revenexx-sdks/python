from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketCurrencyUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    code : Optional[str]
        ISO 4217 code, e.g. EUR (unique per market).
    is_default : Optional[bool]
        Typed model field.
    position : Optional[float]
        Sort position (default 0).
    """
    code: Optional[str] = Field(default=None, alias='code')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    position: Optional[float] = Field(default=None, alias='position')
