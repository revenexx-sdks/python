from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Location(AppwriteModel):
    """
    

    Attributes
    ----------
    address : Optional[Dict[str, Any]]
        Typed model field.
    code : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    enabled : Optional[bool]
        Typed model field.
    id : Optional[str]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Typed model field.
    name : Optional[str]
        Typed model field.
    priority : Optional[float]
        Typed model field.
    type : Optional[str]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    address: Optional[Dict[str, Any]] = Field(default=None, alias='address')
    code: Optional[str] = Field(default=None, alias='code')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    id: Optional[str] = Field(default=None, alias='id')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    priority: Optional[float] = Field(default=None, alias='priority')
    type: Optional[str] = Field(default=None, alias='type')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
