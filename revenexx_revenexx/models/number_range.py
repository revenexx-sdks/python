from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class NumberRange(AppwriteModel):
    """
    

    Attributes
    ----------
    channel_id : Optional[str]
        Typed model field.
    code : Optional[str]
        Typed model field.
    counter : Optional[float]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Typed model field.
    padding : Optional[float]
        Typed model field.
    position_step : Optional[float]
        Typed model field.
    prefix : Optional[str]
        Typed model field.
    step : Optional[float]
        Typed model field.
    suffix : Optional[str]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    code: Optional[str] = Field(default=None, alias='code')
    counter: Optional[float] = Field(default=None, alias='counter')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    padding: Optional[float] = Field(default=None, alias='padding')
    position_step: Optional[float] = Field(default=None, alias='position_step')
    prefix: Optional[str] = Field(default=None, alias='prefix')
    step: Optional[float] = Field(default=None, alias='step')
    suffix: Optional[str] = Field(default=None, alias='suffix')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
