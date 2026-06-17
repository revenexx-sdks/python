from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Market(AppwriteModel):
    """
    

    Attributes
    ----------
    code : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    currency : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    is_default : Optional[bool]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    name : Optional[str]
        Typed model field.
    position : Optional[float]
        Typed model field.
    status : Optional[str]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    code: Optional[str] = Field(default=None, alias='code')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    currency: Optional[str] = Field(default=None, alias='currency')
    id: Optional[str] = Field(default=None, alias='id')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    status: Optional[str] = Field(default=None, alias='status')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
