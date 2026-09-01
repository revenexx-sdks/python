from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CategoryRuleSample(AppwriteModel):
    """
    

    Attributes
    ----------
    id : Optional[str]
        A matching product.
    sku : Optional[str]
        Its SKU, so the sample is readable. Null only for a row whose SKU is unset, which the database does not allow.
    """
    id: Optional[str] = Field(default=None, alias='id')
    sku: Optional[str] = Field(default=None, alias='sku')
