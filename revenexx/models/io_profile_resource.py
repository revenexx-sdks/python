from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.io_profile_resource_apply_mode import IoProfileResourceApplyMode
from ..enums.io_profile_resource_direction import IoProfileResourceDirection
from .io_profile_format import IoProfileFormat

class IoProfileResource(AppwriteModel):
    """
    A saved profile. Mirrors the controller&#039;s presenter exactly — there
are no `created_at` / `updated_at` fields on this resource.


    Attributes
    ----------
    app : Optional[str]
        Typed model field.
    apply_mode : Optional[IoProfileResourceApplyMode]
        Typed model field.
    created_by : Optional[str]
        Typed model field.
    direction : Optional[IoProfileResourceDirection]
        Typed model field.
    entity : Optional[str]
        Typed model field.
    format : Optional[IoProfileFormat]
        Typed model field.
    id : Optional[str]
        Typed model field.
    mapping : Optional[Dict[str, Any]]
        Typed model field.
    markets : Optional[List[Any]]
        `null` means global — offered for every market.
    name : Optional[str]
        Typed model field.
    options : Optional[Dict[str, Any]]
        Typed model field.
    vendor : Optional[str]
        Typed model field.
    """
    app: Optional[str] = Field(default=None, alias='app')
    apply_mode: Optional[IoProfileResourceApplyMode] = Field(default=None, alias='apply_mode')
    created_by: Optional[str] = Field(default=None, alias='created_by')
    direction: Optional[IoProfileResourceDirection] = Field(default=None, alias='direction')
    entity: Optional[str] = Field(default=None, alias='entity')
    format: Optional[IoProfileFormat] = Field(default=None, alias='format')
    id: Optional[str] = Field(default=None, alias='id')
    mapping: Optional[Dict[str, Any]] = Field(default=None, alias='mapping')
    markets: Optional[List[Any]] = Field(default=None, alias='markets')
    name: Optional[str] = Field(default=None, alias='name')
    options: Optional[Dict[str, Any]] = Field(default=None, alias='options')
    vendor: Optional[str] = Field(default=None, alias='vendor')
