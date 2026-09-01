from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PageTemplateCreateRequest(AppwriteModel):
    """
    The blocks to freeze, and where the template should be offered.

    Attributes
    ----------
    description : Optional[str]
        A sentence about when to reach for it.
    fieldname : Optional[str]
        The field this template should be offered in. Null offers it in every field.
    isdefault : Optional[bool]
        Whether a new page of that type should start from this template.
    label : str
        What the template is called in the picker.
    pagebundle : Optional[str]
        The page type this template should be offered on. Omit to take the current page&#039;s own type.
    uuids : List[Any]
        The blocks to serialize into the template, each with its whole subtree. They are read from the CURRENT edit state, so unpublished changes are included.
    """
    description: Optional[str] = Field(default=None, alias='description')
    fieldname: Optional[str] = Field(default=None, alias='fieldName')
    isdefault: Optional[bool] = Field(default=None, alias='isDefault')
    label: str = Field(..., alias='label')
    pagebundle: Optional[str] = Field(default=None, alias='pageBundle')
    uuids: List[Any] = Field(..., alias='uuids')
