from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderPage(AppwriteModel):
    """
    Where this answer sits in the whole result set.

    Attributes
    ----------
    hasmore : Optional[bool]
        Whether another page exists after this one (offset + returned &lt; total). The one field a &quot;load more&quot; button should read.
    limit : Optional[float]
        The page size that was applied. A requested limit above 200 is CLAMPED to 200 rather than refused, so this is the number to believe, not the one you sent.
    offset : Optional[float]
        The row offset that was applied.
    returned : Optional[float]
        How many rows are in `items` right here — less than `limit` on the last page.
    total : Optional[float]
        How many rows match the filter in total, ignoring limit and offset. This is what a page count is computed from.
    """
    hasmore: Optional[bool] = Field(default=None, alias='hasMore')
    limit: Optional[float] = Field(default=None, alias='limit')
    offset: Optional[float] = Field(default=None, alias='offset')
    returned: Optional[float] = Field(default=None, alias='returned')
    total: Optional[float] = Field(default=None, alias='total')
