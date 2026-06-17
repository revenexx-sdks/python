from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MeasurementFamiliesUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    code : Optional[str]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    standard_unit : Optional[str]
        Typed model field.
    units : Optional[Dict[str, Any]]
        Typed model field.
    """
    code: Optional[str] = Field(default=None, alias='code')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    standard_unit: Optional[str] = Field(default=None, alias='standard_unit')
    units: Optional[Dict[str, Any]] = Field(default=None, alias='units')
