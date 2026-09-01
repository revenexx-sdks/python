from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AttributeList(AppwriteModel):
    """
    Attributes List

    Attributes
    ----------
    attributes : List[Any]
        List of attributes.
    total : float
        Total number of attributes in the given collection.
    """
    attributes: List[Any] = Field(..., alias='attributes')
    total: float = Field(..., alias='total')
