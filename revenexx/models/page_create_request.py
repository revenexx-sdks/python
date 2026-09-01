from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PageCreateRequest(AppwriteModel):
    """
    A new page. Only the title is yours to supply — everything else has a tenant default behind it.

    Attributes
    ----------
    bundle : Optional[str]
        The page type. Omit to take the default_page_bundle setting.
    hostoptions : Optional[Dict[str, Any]]
        Page-level blökkli display options as a flat `option key → value` map. Theme-defined; usually left out and set later from the editor.
    meta : Optional[Dict[str, Any]]
        The page&#039;s metadata bag (SEO and social fields). Stored and handed back untouched — this app reads no key of it, so the theme decides what goes in.
    slug : Optional[str]
        The path segment the storefront routes it under, without a leading slash. Unique per tenant among live pages; omit or send null for a page reached only by id. Nothing here derives one from the title.
    sourcelanguage : Optional[str]
        The language you are authoring in, and the fallback for every later translation. Omit to take the default_source_language setting for the request market.
    title : str
        What the page is called, in its source language. Shown in the editorial list and searched by `?q=`.
    """
    bundle: Optional[str] = Field(default=None, alias='bundle')
    hostoptions: Optional[Dict[str, Any]] = Field(default=None, alias='hostOptions')
    meta: Optional[Dict[str, Any]] = Field(default=None, alias='meta')
    slug: Optional[str] = Field(default=None, alias='slug')
    sourcelanguage: Optional[str] = Field(default=None, alias='sourceLanguage')
    title: str = Field(..., alias='title')
