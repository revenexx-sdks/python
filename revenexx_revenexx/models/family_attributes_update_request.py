from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class FamilyAttributesUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    attribute_id : Optional[str]
        Typed model field.
    family_id : Optional[str]
        Typed model field.
    is_required : Optional[bool]
        Typed model field.
    position : Optional[float]
        Typed model field.
    required_channels : Optional[Dict[str, Any]]
        Typed model field.
    """
    attribute_id: Optional[str] = Field(default=None, alias='attribute_id')
    family_id: Optional[str] = Field(default=None, alias='family_id')
    is_required: Optional[bool] = Field(default=None, alias='is_required')
    position: Optional[float] = Field(default=None, alias='position')
    required_channels: Optional[Dict[str, Any]] = Field(default=None, alias='required_channels')
