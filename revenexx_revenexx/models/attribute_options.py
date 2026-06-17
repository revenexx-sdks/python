from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AttributeOptions(AppwriteModel):
    """
    

    Attributes
    ----------
    attribute_id : Optional[str]
        Typed model field.
    code : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    position : Optional[float]
        Typed model field.
    swatch : Optional[Dict[str, Any]]
        Typed model field.
    """
    attribute_id: Optional[str] = Field(default=None, alias='attribute_id')
    code: Optional[str] = Field(default=None, alias='code')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
    swatch: Optional[Dict[str, Any]] = Field(default=None, alias='swatch')
