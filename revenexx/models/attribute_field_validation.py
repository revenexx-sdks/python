from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AttributeFieldValidation(AppwriteModel):
    """
    The limits the value has to satisfy, ready to hand to a form validator. Only the seven keys below are republished; anything else the tenant stored in `attributes.validation` stays there.

    Attributes
    ----------
    max : Optional[float]
        Largest permitted number.
    max_items : Optional[float]
        Most entries.
    max_length : Optional[float]
        Longest permitted text.
    min : Optional[float]
        Smallest permitted number, for a number or measure field.
    min_items : Optional[float]
        Fewest entries, for a multi-select or a collection.
    min_length : Optional[float]
        Shortest permitted text.
    pattern : Optional[str]
        A regular expression the text has to match.
    """
    max: Optional[float] = Field(default=None, alias='max')
    max_items: Optional[float] = Field(default=None, alias='max_items')
    max_length: Optional[float] = Field(default=None, alias='max_length')
    min: Optional[float] = Field(default=None, alias='min')
    min_items: Optional[float] = Field(default=None, alias='min_items')
    min_length: Optional[float] = Field(default=None, alias='min_length')
    pattern: Optional[str] = Field(default=None, alias='pattern')
