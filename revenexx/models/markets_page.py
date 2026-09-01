from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketsPage(AppwriteModel):
    """
    Where in the result set this answer sits. `limit` and `offset` are the values that were APPLIED, not the ones that were asked for — the data plane clamps rather than refuses, so an out-of-range or unparseable value comes back corrected here instead of as a 400.

    Attributes
    ----------
    hasmore : Optional[bool]
        True when `offset + returned &lt; total`, i.e. another page exists. Cheaper to branch on than comparing the three numbers yourself.
    limit : Optional[float]
        Page size actually applied. A request over 200 is clamped to 200, one under 1 (or one that is not a number) to the 50-row default.
    offset : Optional[float]
        Row offset actually applied. A negative offset is clamped to 0.
    returned : Optional[float]
        Rows in `items` on this page. Lower than `limit` on the last page.
    total : Optional[float]
        Rows matching the filter across ALL pages, ignoring limit and offset — the number to paginate against.
    """
    hasmore: Optional[bool] = Field(default=None, alias='hasMore')
    limit: Optional[float] = Field(default=None, alias='limit')
    offset: Optional[float] = Field(default=None, alias='offset')
    returned: Optional[float] = Field(default=None, alias='returned')
    total: Optional[float] = Field(default=None, alias='total')
