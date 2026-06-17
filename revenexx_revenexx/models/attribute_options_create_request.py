from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AttributeOptionsCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    attribute_id : str
        Typed model field.
    code : str
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    position : Optional[float]
        Typed model field.
    swatch : Optional[Dict[str, Any]]
        Typed model field.
    """
    attribute_id: str = Field(..., alias='attribute_id')
    code: str = Field(..., alias='code')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
    swatch: Optional[Dict[str, Any]] = Field(default=None, alias='swatch')
