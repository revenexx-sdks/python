from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .price_list import PriceList

class PriceListMakeDefaultResponse(AppwriteModel):
    """
    The list as it now stands, plus whoever lost the flag.

    Attributes
    ----------
    demoted : Optional[List[Any]]
        Codes of the lists that lost the flag — empty when this list already held it, which is what makes a repeated call free.
    price_list : Optional[PriceList]
        A price list: one currency, one tax basis, one validity window, one buyer scope — and the entries that price items in it. Which list wins for a given buyer is decided by scope first, then priority, then the default flag; see prices.resolve.
    """
    demoted: Optional[List[Any]] = Field(default=None, alias='demoted')
    price_list: Optional[PriceList] = Field(default=None, alias='price_list')
