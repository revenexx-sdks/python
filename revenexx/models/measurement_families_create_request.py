from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MeasurementFamiliesCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        The measurement family&#039;s stable identifier. A `measure` attribute names one and then offers that family&#039;s units.
    labels : Optional[Dict[str, Any]]
        What the measurement family is called, per language tag.
    standard_unit : str
        The unit every value of this family is converted to before it is compared or sorted — the unit each `convert_factor` is relative to.
    units : Optional[Dict[str, Any]]
        The units this family offers. `convert_factor` multiplies a value into `standard_unit`, so a gram is 0.001 kilograms; `symbol` is what a form prints next to the number.
    """
    code: str = Field(..., alias='code')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    standard_unit: str = Field(..., alias='standard_unit')
    units: Optional[Dict[str, Any]] = Field(default=None, alias='units')
