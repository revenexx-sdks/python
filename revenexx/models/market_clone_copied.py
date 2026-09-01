from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketCloneCopied(AppwriteModel):
    """
    Child rows copied from the source, per collection. A flag left false is a zero here, and so is a source that had none of that kind.

    Attributes
    ----------
    currencies : Optional[float]
        Traded currencies copied from the source market.
    locales : Optional[float]
        Locales copied from the source market.
    tax_classes : Optional[float]
        Tax classes copied from the source market.
    """
    currencies: Optional[float] = Field(default=None, alias='currencies')
    locales: Optional[float] = Field(default=None, alias='locales')
    tax_classes: Optional[float] = Field(default=None, alias='tax_classes')
