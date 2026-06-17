from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ProductCategories(AppwriteModel):
    """
    

    Attributes
    ----------
    category_id : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    position : Optional[float]
        Typed model field.
    product_id : Optional[str]
        Typed model field.
    """
    category_id: Optional[str] = Field(default=None, alias='category_id')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    position: Optional[float] = Field(default=None, alias='position')
    product_id: Optional[str] = Field(default=None, alias='product_id')
