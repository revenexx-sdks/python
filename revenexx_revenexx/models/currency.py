from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Currency(AppwriteModel):
    """
    Currency

    Attributes
    ----------
    code : str
        Currency code in [ISO 4217-1](http://en.wikipedia.org/wiki/ISO_4217) three-character format.
    decimaldigits : float
        Number of decimal digits.
    name : str
        Currency name.
    nameplural : str
        Currency plural name
    rounding : float
        Currency digit rounding.
    symbol : str
        Currency symbol.
    symbolnative : str
        Currency native symbol.
    """
    code: str = Field(..., alias='code')
    decimaldigits: float = Field(..., alias='decimalDigits')
    name: str = Field(..., alias='name')
    nameplural: str = Field(..., alias='namePlural')
    rounding: float = Field(..., alias='rounding')
    symbol: str = Field(..., alias='symbol')
    symbolnative: str = Field(..., alias='symbolNative')
