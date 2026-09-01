from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class FormsPage(AppwriteModel):
    """
    Where this page sits in the result set. Everything needed to fetch the next one is here, so a client never has to guess whether it has seen everything.

    Attributes
    ----------
    hasmore : Optional[bool]
        True while `offset + returned &lt; total`: another page follows, at `offset + returned`.
    limit : Optional[float]
        The page size that was applied — the `limit` parameter after clamping to 1…200, or 50 when none was given.
    offset : Optional[float]
        How many matching rows were skipped before this page.
    returned : Optional[float]
        How many rows are in `items` — below `limit` exactly on the last page.
    total : Optional[float]
        How many rows match the filter in total, ignoring the page. This is the number to show a merchant; `returned` is only what fitted.
    """
    hasmore: Optional[bool] = Field(default=None, alias='hasMore')
    limit: Optional[float] = Field(default=None, alias='limit')
    offset: Optional[float] = Field(default=None, alias='offset')
    returned: Optional[float] = Field(default=None, alias='returned')
    total: Optional[float] = Field(default=None, alias='total')
