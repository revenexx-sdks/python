from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_comment_visibility import OrderCommentVisibility

class OrderComment(AppwriteModel):
    """
    A note on an order, either internal between operators or meant for the customer to see.

    Attributes
    ----------
    author : Optional[str]
        Who wrote it, as the caller reported it. Free text; not resolved against a user directory.
    body : Optional[str]
        The comment itself. Plain text; this app neither renders nor sanitizes it.
    created_at : Optional[str]
        When the comment was written. Comments come back oldest first.
    id : Optional[str]
        Primary key of the comment.
    order_id : Optional[str]
        The order the comment hangs on.
    visibility : Optional[OrderCommentVisibility]
        Who may see it: &#039;internal&#039; is a note between operators, &#039;customer&#039; is meant to be shown in the customer&#039;s order view. Nothing here enforces that — this app labels the comment and the client showing it decides. Defaults to the tenant&#039;s default_comment_visibility.
    """
    author: Optional[str] = Field(default=None, alias='author')
    body: Optional[str] = Field(default=None, alias='body')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    order_id: Optional[str] = Field(default=None, alias='order_id')
    visibility: Optional[OrderCommentVisibility] = Field(default=None, alias='visibility')
