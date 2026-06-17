from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MeasurementFamiliesCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    standard_unit : str
        Typed model field.
    units : Optional[Dict[str, Any]]
        Typed model field.
    """
    code: str = Field(..., alias='code')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    standard_unit: str = Field(..., alias='standard_unit')
    units: Optional[Dict[str, Any]] = Field(default=None, alias='units')
