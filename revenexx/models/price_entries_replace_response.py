from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .price_entry import PriceEntry

class PriceEntriesReplaceResponse(AppwriteModel):
    """
    The list as it now stands: everything that was there is gone and these are the rows that took its place.

    Attributes
    ----------
    entries : Optional[List[PriceEntry]]
        The complete new entry set, as stored — including the ids and timestamps the database filled in.
    """
    entries: Optional[List[PriceEntry]] = Field(default=None, alias='entries')
