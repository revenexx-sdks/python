from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.page_status import PageStatus

class PageUpdateRequest(AppwriteModel):
    """
    Partial update — only title, slug, status, meta and bundle are applied; other keys are ignored. The page&#039;s CONTENT is never edited here: blocks change through the editor&#039;s mutation log.

    Attributes
    ----------
    bundle : Optional[str]
        The page type. Changing it changes which template the theme renders.
    meta : Optional[Dict[str, Any]]
        The page&#039;s metadata bag. Replaced wholesale, not merged.
    slug : Optional[str]
        The path segment the storefront routes it under. Sending a slug another live page holds answers 409; sending null makes the page unreachable by path.
    status : Optional[PageStatus]
        The lifecycle status. Setting `published` here does NOT publish content — delivery still needs a revision, which only `POST /pages/editor/{page_id}/publish` writes.
    title : Optional[str]
        The page title in its source language.
    """
    bundle: Optional[str] = Field(default=None, alias='bundle')
    meta: Optional[Dict[str, Any]] = Field(default=None, alias='meta')
    slug: Optional[str] = Field(default=None, alias='slug')
    status: Optional[PageStatus] = Field(default=None, alias='status')
    title: Optional[str] = Field(default=None, alias='title')
