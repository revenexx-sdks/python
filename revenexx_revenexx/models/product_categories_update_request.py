from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ProductCategoriesUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    category_id : Optional[str]
        Typed model field.
    position : Optional[float]
        Typed model field.
    product_id : Optional[str]
        Typed model field.
    """
    category_id: Optional[str] = Field(default=None, alias='category_id')
    position: Optional[float] = Field(default=None, alias='position')
    product_id: Optional[str] = Field(default=None, alias='product_id')
