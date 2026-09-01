from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .page_comment_item import PageCommentItem

class PageCommentList(AppwriteModel):
    """
    Every comment of the page, roots and replies flat in one list, oldest first — the editor builds the threads from `parentUuid`. Every write route answers this same full list rather than the row it changed.

    Attributes
    ----------
    items : Optional[List[PageCommentItem]]
        The page&#039;s comments, oldest first.
    """
    items: Optional[List[PageCommentItem]] = Field(default=None, alias='items')
