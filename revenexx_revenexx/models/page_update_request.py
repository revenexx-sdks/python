from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.page_status import PageStatus

class PageUpdateRequest(AppwriteModel):
    """
    Partial update — only title, slug, status, meta and bundle are applied; other keys are ignored.

    Attributes
    ----------
    bundle : Optional[str]
        Typed model field.
    meta : Optional[Dict[str, Any]]
        Typed model field.
    slug : Optional[str]
        Typed model field.
    status : Optional[PageStatus]
        Typed model field.
    title : Optional[str]
        Typed model field.
    """
    bundle: Optional[str] = Field(default=None, alias='bundle')
    meta: Optional[Dict[str, Any]] = Field(default=None, alias='meta')
    slug: Optional[str] = Field(default=None, alias='slug')
    status: Optional[PageStatus] = Field(default=None, alias='status')
    title: Optional[str] = Field(default=None, alias='title')
