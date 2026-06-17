from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketCurrency(AppwriteModel):
    """
    

    Attributes
    ----------
    code : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    is_default : Optional[bool]
        Typed model field.
    market_id : Optional[str]
        Typed model field.
    position : Optional[float]
        Typed model field.
    """
    code: Optional[str] = Field(default=None, alias='code')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    market_id: Optional[str] = Field(default=None, alias='market_id')
    position: Optional[float] = Field(default=None, alias='position')
