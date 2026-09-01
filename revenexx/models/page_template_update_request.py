from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .page_block_tree import PageBlockTree

class PageTemplateUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value. A template is a COPY source, so changing it never reaches the pages already made from it.

    Attributes
    ----------
    description : Optional[str]
        A sentence about when to reach for it, shown next to the label.
    field_name : Optional[str]
        The field this template is offered in. Null offers it in every field.
    is_default : Optional[bool]
        Whether a new page of this bundle starts from this template.
    label : Optional[str]
        What the template is called in the picker.
    page_bundle : Optional[str]
        The page type this template is offered on. Null offers it on every page type.
    tree : Optional[List[PageBlockTree]]
        The blocks the template inserts, in order. Replaces the stored tree completely.
    """
    description: Optional[str] = Field(default=None, alias='description')
    field_name: Optional[str] = Field(default=None, alias='field_name')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    label: Optional[str] = Field(default=None, alias='label')
    page_bundle: Optional[str] = Field(default=None, alias='page_bundle')
    tree: Optional[List[PageBlockTree]] = Field(default=None, alias='tree')
