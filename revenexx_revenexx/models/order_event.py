from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderEvent(AppwriteModel):
    """
    

    Attributes
    ----------
    actor : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    name : Optional[str]
        Typed model field.
    order_id : Optional[str]
        Typed model field.
    payload : Optional[Dict[str, Any]]
        Typed model field.
    """
    actor: Optional[str] = Field(default=None, alias='actor')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    name: Optional[str] = Field(default=None, alias='name')
    order_id: Optional[str] = Field(default=None, alias='order_id')
    payload: Optional[Dict[str, Any]] = Field(default=None, alias='payload')
