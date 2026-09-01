from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketBackfillKept(AppwriteModel):
    """
    What this market already held BEFORE the repair, per collection — the rows that were left exactly as the merchant left them.

    Attributes
    ----------
    currencies : Optional[float]
        Traded currencies this market already held, untouched.
    locales : Optional[float]
        Locales this market already held, untouched.
    tax_classes : Optional[float]
        Tax classes this market already held, untouched.
    """
    currencies: Optional[float] = Field(default=None, alias='currencies')
    locales: Optional[float] = Field(default=None, alias='locales')
    tax_classes: Optional[float] = Field(default=None, alias='tax_classes')
