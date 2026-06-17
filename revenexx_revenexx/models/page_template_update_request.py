from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PageTemplateUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    description : Optional[str]
        Typed model field.
    field_name : Optional[str]
        Typed model field.
    is_default : Optional[bool]
        Typed model field.
    label : Optional[str]
        Typed model field.
    page_bundle : Optional[str]
        Typed model field.
    tree : Optional[List[Any]]
        Serialized block trees ({ bundle, props, props_i18n, options, children }).
    """
    description: Optional[str] = Field(default=None, alias='description')
    field_name: Optional[str] = Field(default=None, alias='field_name')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    label: Optional[str] = Field(default=None, alias='label')
    page_bundle: Optional[str] = Field(default=None, alias='page_bundle')
    tree: Optional[List[Any]] = Field(default=None, alias='tree')
