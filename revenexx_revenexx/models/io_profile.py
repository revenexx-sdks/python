from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class IoProfile(AppwriteModel):
    """
    

    Attributes
    ----------
    apply_mode : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    direction : Optional[str]
        Typed model field.
    entity : Optional[str]
        Typed model field.
    format : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    is_template : Optional[bool]
        Typed model field.
    mapping : Optional[Dict[str, Any]]
        Typed model field.
    name : Optional[str]
        Typed model field.
    options : Optional[Dict[str, Any]]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    apply_mode: Optional[str] = Field(default=None, alias='apply_mode')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    direction: Optional[str] = Field(default=None, alias='direction')
    entity: Optional[str] = Field(default=None, alias='entity')
    format: Optional[str] = Field(default=None, alias='format')
    id: Optional[str] = Field(default=None, alias='id')
    is_template: Optional[bool] = Field(default=None, alias='is_template')
    mapping: Optional[Dict[str, Any]] = Field(default=None, alias='mapping')
    name: Optional[str] = Field(default=None, alias='name')
    options: Optional[Dict[str, Any]] = Field(default=None, alias='options')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
