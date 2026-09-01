from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PriceListRef(AppwriteModel):
    """
    The price list this answer came out of — enough to link to it or to explain the number to a merchant (&quot;this came from the dealer list&quot;).

    Attributes
    ----------
    code : Optional[str]
        The list’s unique per-tenant code.
    id : Optional[str]
        The list, by id — the same id `GET /prices/lists/{id}` takes.
    """
    code: Optional[str] = Field(default=None, alias='code')
    id: Optional[str] = Field(default=None, alias='id')
