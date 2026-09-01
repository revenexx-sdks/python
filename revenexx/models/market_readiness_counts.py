from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketReadinessCounts(AppwriteModel):
    """
    How much of a market this market actually is. All three at zero is a market that is a row and nothing else — the state two of the three live markets on the platform were left in, and the reason /clone and /backfill exist.

    Attributes
    ----------
    currencies : Optional[float]
        Traded currencies registered on this market.
    locales : Optional[float]
        Locales registered on this market.
    tax_classes : Optional[float]
        Tax classes registered on this market.
    """
    currencies: Optional[float] = Field(default=None, alias='currencies')
    locales: Optional[float] = Field(default=None, alias='locales')
    tax_classes: Optional[float] = Field(default=None, alias='tax_classes')
