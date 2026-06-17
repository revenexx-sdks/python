from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Categories(AppwriteModel):
    """
    

    Attributes
    ----------
    code : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    parent_id : Optional[str]
        Typed model field.
    path : Optional[str]
        Typed model field.
    position : Optional[float]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    values : Optional[Dict[str, Any]]
        Typed model field.
    """
    code: Optional[str] = Field(default=None, alias='code')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    parent_id: Optional[str] = Field(default=None, alias='parent_id')
    path: Optional[str] = Field(default=None, alias='path')
    position: Optional[float] = Field(default=None, alias='position')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
    values: Optional[Dict[str, Any]] = Field(default=None, alias='values')
