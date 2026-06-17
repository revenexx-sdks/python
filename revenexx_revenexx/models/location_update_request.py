from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.location_type import LocationType

class LocationUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    address : Optional[Dict[str, Any]]
        Typed model field.
    code : Optional[str]
        Unique location code (per tenant).
    enabled : Optional[bool]
        Disabled locations are skipped by availability and reserve (default true).
    labels : Optional[Dict[str, Any]]
        Localised display names ({de, en, …}).
    metadata : Optional[Dict[str, Any]]
        Free-form metadata.
    name : Optional[str]
        Typed model field.
    priority : Optional[float]
        Sourcing order — lower wins (default 0).
    type : Optional[LocationType]
        Default &#039;warehouse&#039;.
    """
    address: Optional[Dict[str, Any]] = Field(default=None, alias='address')
    code: Optional[str] = Field(default=None, alias='code')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    priority: Optional[float] = Field(default=None, alias='priority')
    type: Optional[LocationType] = Field(default=None, alias='type')
