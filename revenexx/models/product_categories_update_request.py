from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.product_categories_source import ProductCategoriesSource

class ProductCategoriesUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    category_id : Optional[str]
        The category it is filed into. One row per (product, category), whichever way it got there.
    position : Optional[float]
        Sort order of this product inside the category.
    product_id : Optional[str]
        The product filed into the category. Deleting the product deletes the membership with it.
    source : Optional[ProductCategoriesSource]
        How the membership came about: &#039;manual&#039; is hand-picked, &#039;rule&#039; was materialized by a category rule. The two never touch each other — a recompute only ever inserts and deletes `rule` rows, so a hand-picked membership survives every pass.
    """
    category_id: Optional[str] = Field(default=None, alias='category_id')
    position: Optional[float] = Field(default=None, alias='position')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    source: Optional[ProductCategoriesSource] = Field(default=None, alias='source')
