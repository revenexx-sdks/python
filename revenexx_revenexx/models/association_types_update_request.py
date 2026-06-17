from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AssociationTypesUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    code : Optional[str]
        Typed model field.
    is_quantified : Optional[bool]
        Typed model field.
    is_two_way : Optional[bool]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    """
    code: Optional[str] = Field(default=None, alias='code')
    is_quantified: Optional[bool] = Field(default=None, alias='is_quantified')
    is_two_way: Optional[bool] = Field(default=None, alias='is_two_way')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
