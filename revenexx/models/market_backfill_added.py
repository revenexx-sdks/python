from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketBackfillAdded(AppwriteModel):
    """
    Child rows copied in from the source, per collection — only codes this market did not already carry. Zero everywhere on a second run: the call is idempotent.

    Attributes
    ----------
    currencies : Optional[float]
        Traded currencies added from the source market.
    locales : Optional[float]
        Locales added from the source market.
    tax_classes : Optional[float]
        Tax classes added from the source market.
    """
    currencies: Optional[float] = Field(default=None, alias='currencies')
    locales: Optional[float] = Field(default=None, alias='locales')
    tax_classes: Optional[float] = Field(default=None, alias='tax_classes')
