from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AttributesCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        Typed model field.
    config : Optional[Dict[str, Any]]
        Typed model field.
    entity_ref : Optional[str]
        Typed model field.
    entity_type : Optional[str]
        Typed model field.
    group_id : Optional[str]
        Typed model field.
    is_filterable : Optional[bool]
        Typed model field.
    is_unique : Optional[bool]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    localizable : Optional[bool]
        Typed model field.
    position : Optional[float]
        Typed model field.
    scopable : Optional[bool]
        Typed model field.
    type : str
        Typed model field.
    usable_in_grid : Optional[bool]
        Typed model field.
    validation : Optional[Dict[str, Any]]
        Typed model field.
    """
    code: str = Field(..., alias='code')
    config: Optional[Dict[str, Any]] = Field(default=None, alias='config')
    entity_ref: Optional[str] = Field(default=None, alias='entity_ref')
    entity_type: Optional[str] = Field(default=None, alias='entity_type')
    group_id: Optional[str] = Field(default=None, alias='group_id')
    is_filterable: Optional[bool] = Field(default=None, alias='is_filterable')
    is_unique: Optional[bool] = Field(default=None, alias='is_unique')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    localizable: Optional[bool] = Field(default=None, alias='localizable')
    position: Optional[float] = Field(default=None, alias='position')
    scopable: Optional[bool] = Field(default=None, alias='scopable')
    type: str = Field(..., alias='type')
    usable_in_grid: Optional[bool] = Field(default=None, alias='usable_in_grid')
    validation: Optional[Dict[str, Any]] = Field(default=None, alias='validation')
