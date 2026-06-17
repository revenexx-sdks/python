from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AssetFamilies(AppwriteModel):
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
    naming_convention : Optional[Dict[str, Any]]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    code: Optional[str] = Field(default=None, alias='code')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    naming_convention: Optional[Dict[str, Any]] = Field(default=None, alias='naming_convention')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
