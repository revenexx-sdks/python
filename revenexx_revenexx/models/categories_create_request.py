from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CategoriesCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    parent_id : Optional[str]
        Typed model field.
    path : Optional[str]
        Typed model field.
    position : Optional[float]
        Typed model field.
    values : Optional[Dict[str, Any]]
        Typed model field.
    """
    code: str = Field(..., alias='code')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    parent_id: Optional[str] = Field(default=None, alias='parent_id')
    path: Optional[str] = Field(default=None, alias='path')
    position: Optional[float] = Field(default=None, alias='position')
    values: Optional[Dict[str, Any]] = Field(default=None, alias='values')
