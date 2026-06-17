from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Families(AppwriteModel):
    """
    

    Attributes
    ----------
    code : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    image_attribute : Optional[str]
        Typed model field.
    label_attribute : Optional[str]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    code: Optional[str] = Field(default=None, alias='code')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    image_attribute: Optional[str] = Field(default=None, alias='image_attribute')
    label_attribute: Optional[str] = Field(default=None, alias='label_attribute')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
