from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ProductTaxRef(AppwriteModel):
    """
    

    Attributes
    ----------
    id : Optional[str]
        Typed model field.
    sku : Optional[str]
        Typed model field.
    tax_class : Optional[str]
        Typed model field.
    """
    id: Optional[str] = Field(default=None, alias='id')
    sku: Optional[str] = Field(default=None, alias='sku')
    tax_class: Optional[str] = Field(default=None, alias='tax_class')
