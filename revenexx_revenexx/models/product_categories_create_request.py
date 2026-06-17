from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ProductCategoriesCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    category_id : str
        Typed model field.
    position : Optional[float]
        Typed model field.
    product_id : str
        Typed model field.
    """
    category_id: str = Field(..., alias='category_id')
    position: Optional[float] = Field(default=None, alias='position')
    product_id: str = Field(..., alias='product_id')
