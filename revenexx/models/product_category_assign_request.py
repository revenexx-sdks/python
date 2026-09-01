from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ProductCategoryAssignRequest(AppwriteModel):
    """
    The category has to exist already; this route files a product into one, it does not create one.

    Attributes
    ----------
    category_id : str
        The category to file the product into.
    position : Optional[float]
        Sort order inside the category. Default 0.
    """
    category_id: str = Field(..., alias='category_id')
    position: Optional[float] = Field(default=None, alias='position')
