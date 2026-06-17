from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Comment(AppwriteModel):
    """
    

    Attributes
    ----------
    author_id : Optional[str]
        Typed model field.
    author_name : Optional[str]
        Typed model field.
    block_uuids : Optional[Dict[str, Any]]
        Typed model field.
    body : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    page_id : Optional[str]
        Typed model field.
    parent_id : Optional[str]
        Typed model field.
    resolved : Optional[bool]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    author_id: Optional[str] = Field(default=None, alias='author_id')
    author_name: Optional[str] = Field(default=None, alias='author_name')
    block_uuids: Optional[Dict[str, Any]] = Field(default=None, alias='block_uuids')
    body: Optional[str] = Field(default=None, alias='body')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    page_id: Optional[str] = Field(default=None, alias='page_id')
    parent_id: Optional[str] = Field(default=None, alias='parent_id')
    resolved: Optional[bool] = Field(default=None, alias='resolved')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
