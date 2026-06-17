from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .market_currency import MarketCurrency
from .market_locale import MarketLocale
from .market import Market
from .market_tax_class import MarketTaxClass

class MarketContext(AppwriteModel):
    """
    

    Attributes
    ----------
    currencies : Optional[List[MarketCurrency]]
        Typed model field.
    locales : Optional[List[MarketLocale]]
        Typed model field.
    market : Optional[Market]
        Typed model field.
    tax_classes : Optional[List[MarketTaxClass]]
        Typed model field.
    """
    currencies: Optional[List[MarketCurrency]] = Field(default=None, alias='currencies')
    locales: Optional[List[MarketLocale]] = Field(default=None, alias='locales')
    market: Optional[Market] = Field(default=None, alias='market')
    tax_classes: Optional[List[MarketTaxClass]] = Field(default=None, alias='tax_classes')
