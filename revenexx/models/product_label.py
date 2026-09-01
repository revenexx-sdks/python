from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.product_label_attribute_source import ProductLabelAttributeSource
from ..enums.product_label_source import ProductLabelSource

class ProductLabel(AppwriteModel):
    """
    

    Attributes
    ----------
    attribute : Optional[str]
        The attribute code the name was read from.
    attribute_from : Optional[ProductLabelAttributeSource]
        How that attribute was chosen: &#039;family&#039; is the product&#039;s own `families.label_attribute`, &#039;setting&#039; the tenant&#039;s `default_label_attribute`, &#039;convention&#039; the built-in fallback to `name` when neither says anything.
    id : Optional[str]
        The product&#039;s id.
    label : Optional[str]
        The name to show. Never empty — read `source` before treating it as a name, because `sku` there means this is the SKU standing in for one.
    locale : Optional[str]
        Which locale the value came out of, when it came from a locale bucket. Null for a value in `common` and for the SKU fallback.
    sku : Optional[str]
        The SKU, which is also the fallback shown as `label` when the catalog holds no name.
    source : Optional[ProductLabelSource]
        Which bucket of attribute_values the name came from. &#039;sku&#039; means the catalog holds no name for this product — show that as a missing name, not as a name.
    """
    attribute: Optional[str] = Field(default=None, alias='attribute')
    attribute_from: Optional[ProductLabelAttributeSource] = Field(default=None, alias='attribute_from')
    id: Optional[str] = Field(default=None, alias='id')
    label: Optional[str] = Field(default=None, alias='label')
    locale: Optional[str] = Field(default=None, alias='locale')
    sku: Optional[str] = Field(default=None, alias='sku')
    source: Optional[ProductLabelSource] = Field(default=None, alias='source')
