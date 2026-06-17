from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ReferenceEntitiesCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        Typed model field.
    image : Optional[str]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    """
    code: str = Field(..., alias='code')
    image: Optional[str] = Field(default=None, alias='image')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
