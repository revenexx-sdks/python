from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class FamilyAttributes(AppwriteModel):
    """
    

    Attributes
    ----------
    attribute_id : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    family_id : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    is_required : Optional[bool]
        Typed model field.
    position : Optional[float]
        Typed model field.
    required_channels : Optional[Dict[str, Any]]
        Typed model field.
    """
    attribute_id: Optional[str] = Field(default=None, alias='attribute_id')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    family_id: Optional[str] = Field(default=None, alias='family_id')
    id: Optional[str] = Field(default=None, alias='id')
    is_required: Optional[bool] = Field(default=None, alias='is_required')
    position: Optional[float] = Field(default=None, alias='position')
    required_channels: Optional[Dict[str, Any]] = Field(default=None, alias='required_channels')
