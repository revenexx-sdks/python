from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderCancellation(AppwriteModel):
    """
    

    Attributes
    ----------
    cancelled_by : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    order_id : Optional[str]
        Typed model field.
    positions : Optional[Dict[str, Any]]
        Typed model field.
    reason : Optional[str]
        Typed model field.
    scope : Optional[str]
        Typed model field.
    """
    cancelled_by: Optional[str] = Field(default=None, alias='cancelled_by')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    order_id: Optional[str] = Field(default=None, alias='order_id')
    positions: Optional[Dict[str, Any]] = Field(default=None, alias='positions')
    reason: Optional[str] = Field(default=None, alias='reason')
    scope: Optional[str] = Field(default=None, alias='scope')
