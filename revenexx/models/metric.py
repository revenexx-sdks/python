from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Metric(AppwriteModel):
    """
    Metric

    Attributes
    ----------
    date : str
        The date at which this metric was aggregated in ISO 8601 format.
    value : float
        The value of this metric at the timestamp.
    """
    date: str = Field(..., alias='date')
    value: float = Field(..., alias='value')
