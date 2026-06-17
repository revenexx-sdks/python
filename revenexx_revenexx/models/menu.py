from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Menu(AppwriteModel):
    """
    

    Attributes
    ----------
    created_at : Optional[str]
        Typed model field.
    created_by : Optional[str]
        Typed model field.
    deleted_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    items : Optional[Dict[str, Any]]
        Typed model field.
    label : Optional[str]
        Typed model field.
    menu_key : Optional[str]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    created_by: Optional[str] = Field(default=None, alias='created_by')
    deleted_at: Optional[str] = Field(default=None, alias='deleted_at')
    id: Optional[str] = Field(default=None, alias='id')
    items: Optional[Dict[str, Any]] = Field(default=None, alias='items')
    label: Optional[str] = Field(default=None, alias='label')
    menu_key: Optional[str] = Field(default=None, alias='menu_key')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
