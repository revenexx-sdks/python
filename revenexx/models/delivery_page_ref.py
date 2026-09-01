from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class DeliveryPageRef(AppwriteModel):
    """
    Just enough of a published page to link to it. The block tree is not here — fetch it with `GET /pages/delivery/page`.

    Attributes
    ----------
    bundle : Optional[str]
        The page type, so a sitemap can group or a picker can filter.
    id : Optional[str]
        The page id, usable as `?id=` on the delivery route.
    slug : Optional[str]
        The path segment to build the URL from. `null` for a page reachable only by id, which a sitemap should skip.
    title : Optional[str]
        The page title in its source language — this projection is not language-resolved.
    """
    bundle: Optional[str] = Field(default=None, alias='bundle')
    id: Optional[str] = Field(default=None, alias='id')
    slug: Optional[str] = Field(default=None, alias='slug')
    title: Optional[str] = Field(default=None, alias='title')
