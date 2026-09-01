from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ProductTaxRef(AppwriteModel):
    """
    

    Attributes
    ----------
    id : Optional[str]
        The product&#039;s id.
    label : Optional[str]
        The product&#039;s resolved display name, or its SKU when the catalog holds no name for it.
    sku : Optional[str]
        The SKU, so a caller that asked by id can key its own answer by SKU and the other way round.
    tax_class : Optional[str]
        The tax class key the prices app resolves a rate from. Null means the product names none and the caller has to fall back to its own default.
    """
    id: Optional[str] = Field(default=None, alias='id')
    label: Optional[str] = Field(default=None, alias='label')
    sku: Optional[str] = Field(default=None, alias='sku')
    tax_class: Optional[str] = Field(default=None, alias='tax_class')
