from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketTaxClassUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    code : Optional[str]
        Tax class code (unique per market).
    is_default : Optional[bool]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Localized display names ({locale: label}).
    name : Optional[str]
        Typed model field.
    position : Optional[float]
        Sort position (default 0).
    rate : Optional[float]
        Tax rate in percent, 0–100 (default 0).
    """
    code: Optional[str] = Field(default=None, alias='code')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    rate: Optional[float] = Field(default=None, alias='rate')
