from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_comment_visibility import OrderCommentVisibility

class OrderCommentCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    author : Optional[str]
        Who wrote it, as the caller reported it. Free text; not resolved against a user directory.
    body : str
        The comment itself. Plain text; this app neither renders nor sanitizes it.
    visibility : Optional[OrderCommentVisibility]
        Who may see it: &#039;internal&#039; is a note between operators, &#039;customer&#039; is meant to be shown in the customer&#039;s order view. Nothing here enforces that — this app labels the comment and the client showing it decides. Defaults to the tenant&#039;s default_comment_visibility. Defaults to the tenant&#039;s default_comment_visibility setting, which is &#039;internal&#039; out of the box.
    """
    author: Optional[str] = Field(default=None, alias='author')
    body: str = Field(..., alias='body')
    visibility: Optional[OrderCommentVisibility] = Field(default=None, alias='visibility')
