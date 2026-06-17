from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class FamilyVariantsUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    axes : Optional[Dict[str, Any]]
        Typed model field.
    code : Optional[str]
        Typed model field.
    family_id : Optional[str]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    """
    axes: Optional[Dict[str, Any]] = Field(default=None, alias='axes')
    code: Optional[str] = Field(default=None, alias='code')
    family_id: Optional[str] = Field(default=None, alias='family_id')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
