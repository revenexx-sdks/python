from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ProductAssociations(AppwriteModel):
    """
    

    Attributes
    ----------
    association_type_id : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    position : Optional[float]
        Typed model field.
    product_id : Optional[str]
        Typed model field.
    quantity : Optional[float]
        Typed model field.
    target_product_id : Optional[str]
        Typed model field.
    """
    association_type_id: Optional[str] = Field(default=None, alias='association_type_id')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    position: Optional[float] = Field(default=None, alias='position')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    target_product_id: Optional[str] = Field(default=None, alias='target_product_id')
