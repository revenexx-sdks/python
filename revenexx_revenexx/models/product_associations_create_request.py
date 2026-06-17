from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ProductAssociationsCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    association_type_id : str
        Typed model field.
    position : Optional[float]
        Typed model field.
    product_id : str
        Typed model field.
    quantity : Optional[float]
        Typed model field.
    target_product_id : str
        Typed model field.
    """
    association_type_id: str = Field(..., alias='association_type_id')
    position: Optional[float] = Field(default=None, alias='position')
    product_id: str = Field(..., alias='product_id')
    quantity: Optional[float] = Field(default=None, alias='quantity')
    target_product_id: str = Field(..., alias='target_product_id')
