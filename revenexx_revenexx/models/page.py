from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Page(AppwriteModel):
    """
    

    Attributes
    ----------
    analyze_ignored : Optional[Dict[str, Any]]
        Typed model field.
    bundle : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    created_by : Optional[str]
        Typed model field.
    deleted_at : Optional[str]
        Typed model field.
    host_options : Optional[Dict[str, Any]]
        Typed model field.
    id : Optional[str]
        Typed model field.
    meta : Optional[Dict[str, Any]]
        Typed model field.
    published_revision_id : Optional[str]
        Typed model field.
    slug : Optional[str]
        Typed model field.
    source_language : Optional[str]
        Typed model field.
    status : Optional[str]
        Typed model field.
    title : Optional[str]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    updated_by : Optional[str]
        Typed model field.
    """
    analyze_ignored: Optional[Dict[str, Any]] = Field(default=None, alias='analyze_ignored')
    bundle: Optional[str] = Field(default=None, alias='bundle')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    created_by: Optional[str] = Field(default=None, alias='created_by')
    deleted_at: Optional[str] = Field(default=None, alias='deleted_at')
    host_options: Optional[Dict[str, Any]] = Field(default=None, alias='host_options')
    id: Optional[str] = Field(default=None, alias='id')
    meta: Optional[Dict[str, Any]] = Field(default=None, alias='meta')
    published_revision_id: Optional[str] = Field(default=None, alias='published_revision_id')
    slug: Optional[str] = Field(default=None, alias='slug')
    source_language: Optional[str] = Field(default=None, alias='source_language')
    status: Optional[str] = Field(default=None, alias='status')
    title: Optional[str] = Field(default=None, alias='title')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
    updated_by: Optional[str] = Field(default=None, alias='updated_by')
