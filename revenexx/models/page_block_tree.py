from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PageBlockTree(AppwriteModel):
    """
    The block and everything under it, serialized. This is the payload: every page that references the item renders THIS tree, so editing it here changes every placement at once.

    Attributes
    ----------
    bundle : Optional[str]
        The block type — `hero`, `text`, `teaser`, whatever the active theme defines. It decides which component renders it and which props it carries.
    children : Optional[Dict[str, Any]]
        Nested blocks, keyed by the field they sit in — `{ &quot;content&quot;: [...], &quot;buttons&quot;: [...] }`. Absent on a leaf block.
    fragment_name : Optional[str]
        The theme fragment this block renders instead of a props-driven component, or `null` for an ordinary block. Theme-defined, like a bundle.
    options : Optional[Dict[str, Any]]
        blökkli display options for this block, as a flat `option key → value` map (variant, spacing, background). Theme-defined, set by the `update_options` mutation.
    props : Optional[Dict[str, Any]]
        The block&#039;s field values in the page&#039;s SOURCE language, as a flat `field name → value` map. The field names are the theme&#039;s; this app stores and replays them without reading one.
    props_i18n : Optional[Dict[str, Any]]
        Per-language overrides of `props`, keyed by langcode: `{ &quot;en&quot;: { &quot;title&quot;: &quot;About us&quot; } }`. A field missing for a language falls back to `props`, which is why a half-translated page still renders.
    """
    bundle: Optional[str] = Field(default=None, alias='bundle')
    children: Optional[Dict[str, Any]] = Field(default=None, alias='children')
    fragment_name: Optional[str] = Field(default=None, alias='fragment_name')
    options: Optional[Dict[str, Any]] = Field(default=None, alias='options')
    props: Optional[Dict[str, Any]] = Field(default=None, alias='props')
    props_i18n: Optional[Dict[str, Any]] = Field(default=None, alias='props_i18n')
