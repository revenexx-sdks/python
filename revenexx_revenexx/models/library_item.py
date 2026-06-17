from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class LibraryItem(AppwriteModel):
    """
    

    Attributes
    ----------
    bundle : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    created_by : Optional[str]
        Typed model field.
    deleted_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    label : Optional[str]
        Typed model field.
    tree : Optional[Dict[str, Any]]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    bundle: Optional[str] = Field(default=None, alias='bundle')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    created_by: Optional[str] = Field(default=None, alias='created_by')
    deleted_at: Optional[str] = Field(default=None, alias='deleted_at')
    id: Optional[str] = Field(default=None, alias='id')
    label: Optional[str] = Field(default=None, alias='label')
    tree: Optional[Dict[str, Any]] = Field(default=None, alias='tree')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
