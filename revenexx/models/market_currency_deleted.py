from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketCurrencyDeleted(AppwriteModel):
    """
    Confirmation that the currency of a market is gone. The row itself is not returned — read it before deleting if you need it.

    Attributes
    ----------
    deleted : Optional[bool]
        Always true — a row that was not there is a 404, not a false.
    id : Optional[str]
        The id of the row that was deleted.
    """
    deleted: Optional[bool] = Field(default=None, alias='deleted')
    id: Optional[str] = Field(default=None, alias='id')
