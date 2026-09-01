from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .currency import Currency

class CurrencyList(AppwriteModel):
    """
    Currencies List

    Attributes
    ----------
    currencies : List[Currency]
        List of currencies.
    total : float
        Total number of currencies that matched your query.
    """
    currencies: List[Currency] = Field(..., alias='currencies')
    total: float = Field(..., alias='total')
