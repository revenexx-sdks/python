from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderComment(AppwriteModel):
    """
    

    Attributes
    ----------
    author : Optional[str]
        Typed model field.
    body : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    order_id : Optional[str]
        Typed model field.
    visibility : Optional[str]
        Typed model field.
    """
    author: Optional[str] = Field(default=None, alias='author')
    body: Optional[str] = Field(default=None, alias='body')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    order_id: Optional[str] = Field(default=None, alias='order_id')
    visibility: Optional[str] = Field(default=None, alias='visibility')
