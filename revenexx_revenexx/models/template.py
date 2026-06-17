from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Template(AppwriteModel):
    """
    

    Attributes
    ----------
    created_at : Optional[str]
        Typed model field.
    created_by : Optional[str]
        Typed model field.
    description : Optional[str]
        Typed model field.
    field_name : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    is_default : Optional[bool]
        Typed model field.
    label : Optional[str]
        Typed model field.
    page_bundle : Optional[str]
        Typed model field.
    tree : Optional[Dict[str, Any]]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    created_by: Optional[str] = Field(default=None, alias='created_by')
    description: Optional[str] = Field(default=None, alias='description')
    field_name: Optional[str] = Field(default=None, alias='field_name')
    id: Optional[str] = Field(default=None, alias='id')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    label: Optional[str] = Field(default=None, alias='label')
    page_bundle: Optional[str] = Field(default=None, alias='page_bundle')
    tree: Optional[Dict[str, Any]] = Field(default=None, alias='tree')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
