from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ItemAvailability(AppwriteModel):
    """
    

    Attributes
    ----------
    available : Optional[float]
        Typed model field.
    locations : Optional[List[Any]]
        Typed model field.
    on_hand : Optional[float]
        Typed model field.
    orderable : Optional[bool]
        Typed model field.
    product_id : Optional[str]
        Typed model field.
    requested : Optional[float]
        Typed model field.
    reserved : Optional[float]
        Typed model field.
    sku : Optional[str]
        Typed model field.
    tracked : Optional[bool]
        false = unknown to inventory; the storefront decides whether untracked items sell freely.
    """
    available: Optional[float] = Field(default=None, alias='available')
    locations: Optional[List[Any]] = Field(default=None, alias='locations')
    on_hand: Optional[float] = Field(default=None, alias='on_hand')
    orderable: Optional[bool] = Field(default=None, alias='orderable')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    requested: Optional[float] = Field(default=None, alias='requested')
    reserved: Optional[float] = Field(default=None, alias='reserved')
    sku: Optional[str] = Field(default=None, alias='sku')
    tracked: Optional[bool] = Field(default=None, alias='tracked')
