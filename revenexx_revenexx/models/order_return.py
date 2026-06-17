from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderReturn(AppwriteModel):
    """
    

    Attributes
    ----------
    completed_at : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Typed model field.
    number : Optional[str]
        Typed model field.
    order_id : Optional[str]
        Typed model field.
    positions : Optional[Dict[str, Any]]
        Typed model field.
    reason : Optional[str]
        Typed model field.
    received_at : Optional[str]
        Typed model field.
    registered_at : Optional[str]
        Typed model field.
    rejected_at : Optional[str]
        Typed model field.
    resolution : Optional[str]
        Typed model field.
    status : Optional[str]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    completed_at: Optional[str] = Field(default=None, alias='completed_at')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    number: Optional[str] = Field(default=None, alias='number')
    order_id: Optional[str] = Field(default=None, alias='order_id')
    positions: Optional[Dict[str, Any]] = Field(default=None, alias='positions')
    reason: Optional[str] = Field(default=None, alias='reason')
    received_at: Optional[str] = Field(default=None, alias='received_at')
    registered_at: Optional[str] = Field(default=None, alias='registered_at')
    rejected_at: Optional[str] = Field(default=None, alias='rejected_at')
    resolution: Optional[str] = Field(default=None, alias='resolution')
    status: Optional[str] = Field(default=None, alias='status')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
