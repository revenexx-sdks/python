from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class FamiliesCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        Typed model field.
    image_attribute : Optional[str]
        Typed model field.
    label_attribute : Optional[str]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    """
    code: str = Field(..., alias='code')
    image_attribute: Optional[str] = Field(default=None, alias='image_attribute')
    label_attribute: Optional[str] = Field(default=None, alias='label_attribute')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
