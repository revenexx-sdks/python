from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketTaxClassCreateRequest(AppwriteModel):
    """
    The owning market comes from the route path (&#039;market_id&#039;).

    Attributes
    ----------
    code : str
        Tax class code (unique per market).
    is_default : Optional[bool]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Localized display names ({locale: label}).
    name : str
        Typed model field.
    position : Optional[float]
        Sort position (default 0).
    rate : Optional[float]
        Tax rate in percent, 0–100 (default 0).
    """
    code: str = Field(..., alias='code')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    name: str = Field(..., alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    rate: Optional[float] = Field(default=None, alias='rate')
