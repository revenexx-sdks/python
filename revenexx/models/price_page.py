from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PricePage(AppwriteModel):
    """
    Where this page sits in the full result set. Rows beyond `limit` are not returned and are not lost — ask for the next page with `offset`.

    Attributes
    ----------
    hasmore : Optional[bool]
        true when `offset + returned &lt; total` — there is another page to fetch.
    limit : Optional[float]
        Page size actually applied — the `limit` you sent, clamped to 1…200 (default 50).
    offset : Optional[float]
        Row offset actually applied (default 0).
    returned : Optional[float]
        Rows in `items` on this page.
    total : Optional[float]
        Rows matching the filter across all pages, not just this one.
    """
    hasmore: Optional[bool] = Field(default=None, alias='hasMore')
    limit: Optional[float] = Field(default=None, alias='limit')
    offset: Optional[float] = Field(default=None, alias='offset')
    returned: Optional[float] = Field(default=None, alias='returned')
    total: Optional[float] = Field(default=None, alias='total')
