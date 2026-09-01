from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class DeliveryBlock(AppwriteModel):
    """
    One block, ready to render: props resolved for the requested language, library references already expanded, scheduled blocks already filtered out.

    Attributes
    ----------
    bundle : Optional[str]
        The block type. This is what a theme switches its component on.
    children : Optional[Dict[str, Any]]
        Nested blocks keyed by the field they sit in — `{ &quot;columns&quot;: [...] }`. Empty object on a leaf block.
    fragmentname : Optional[str]
        The theme fragment to render instead of a props-driven component. Theme-defined, like a bundle.
    libraryitemid : Optional[str]
        The library item this block came from, or `null`. Its content is already inlined above — this is for cache invalidation and editor links, not for a second fetch.
    options : Optional[Dict[str, Any]]
        Display options for this block, as a flat `option key → value` map.
    props : Optional[Dict[str, Any]]
        The block&#039;s field values for the requested language, source values already overlaid with that language&#039;s overrides. Theme-defined keys.
    uuid : Optional[str]
        The block uuid — stable across publishes, so it is safe to use as a render key or an anchor.
    """
    bundle: Optional[str] = Field(default=None, alias='bundle')
    children: Optional[Dict[str, Any]] = Field(default=None, alias='children')
    fragmentname: Optional[str] = Field(default=None, alias='fragmentName')
    libraryitemid: Optional[str] = Field(default=None, alias='libraryItemId')
    options: Optional[Dict[str, Any]] = Field(default=None, alias='options')
    props: Optional[Dict[str, Any]] = Field(default=None, alias='props')
    uuid: Optional[str] = Field(default=None, alias='uuid')
