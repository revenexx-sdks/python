from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AssociationTypes(AppwriteModel):
    """
    

    Attributes
    ----------
    code : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    is_quantified : Optional[bool]
        Typed model field.
    is_two_way : Optional[bool]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    """
    code: Optional[str] = Field(default=None, alias='code')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    is_quantified: Optional[bool] = Field(default=None, alias='is_quantified')
    is_two_way: Optional[bool] = Field(default=None, alias='is_two_way')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
