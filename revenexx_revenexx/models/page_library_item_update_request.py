from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PageLibraryItemUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    bundle : Optional[str]
        Typed model field.
    label : Optional[str]
        Typed model field.
    tree : Optional[Dict[str, Any]]
        Serialized block tree ({ bundle, props, props_i18n, options, children }).
    """
    bundle: Optional[str] = Field(default=None, alias='bundle')
    label: Optional[str] = Field(default=None, alias='label')
    tree: Optional[Dict[str, Any]] = Field(default=None, alias='tree')
