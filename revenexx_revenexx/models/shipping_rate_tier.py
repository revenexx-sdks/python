from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ShippingRateTier(AppwriteModel):
    """
    

    Attributes
    ----------
    created_at : Optional[str]
        Typed model field.
    from_value : Optional[float]
        Typed model field.
    id : Optional[str]
        Typed model field.
    method_id : Optional[str]
        Typed model field.
    position : Optional[float]
        Typed model field.
    price : Optional[float]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    from_value: Optional[float] = Field(default=None, alias='from_value')
    id: Optional[str] = Field(default=None, alias='id')
    method_id: Optional[str] = Field(default=None, alias='method_id')
    position: Optional[float] = Field(default=None, alias='position')
    price: Optional[float] = Field(default=None, alias='price')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
