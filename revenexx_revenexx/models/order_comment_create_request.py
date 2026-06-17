from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_comment_visibility import OrderCommentVisibility

class OrderCommentCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    author : Optional[str]
        Typed model field.
    body : str
        Typed model field.
    visibility : Optional[OrderCommentVisibility]
        Default &#039;internal&#039;.
    """
    author: Optional[str] = Field(default=None, alias='author')
    body: str = Field(..., alias='body')
    visibility: Optional[OrderCommentVisibility] = Field(default=None, alias='visibility')
