from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AssociationTypesCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        Typed model field.
    is_quantified : Optional[bool]
        Typed model field.
    is_two_way : Optional[bool]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    """
    code: str = Field(..., alias='code')
    is_quantified: Optional[bool] = Field(default=None, alias='is_quantified')
    is_two_way: Optional[bool] = Field(default=None, alias='is_two_way')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
