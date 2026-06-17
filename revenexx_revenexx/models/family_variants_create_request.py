from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class FamilyVariantsCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    axes : Optional[Dict[str, Any]]
        Typed model field.
    code : str
        Typed model field.
    family_id : str
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    """
    axes: Optional[Dict[str, Any]] = Field(default=None, alias='axes')
    code: str = Field(..., alias='code')
    family_id: str = Field(..., alias='family_id')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
