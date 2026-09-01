from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.product_label_source import ProductLabelSource

class ProductGridRow(AppwriteModel):
    """
    

    Attributes
    ----------
    attributes : Optional[Dict[str, Any]]
        The grid cells: one key per attribute code that `columns` lists with `source: &quot;attribute&quot;`, holding the value already resolved out of `attribute_values` for the requested context. A code the product carries no value for is null rather than absent, so a row is the same shape whatever it holds. The keys are the tenant&#039;s own attribute codes, which is why this object has no fixed properties — read `columns` for the set.
    completeness : Optional[Dict[str, Any]]
        The stored `products.completeness` document, verbatim. Null means it has never been computed — not that the product is empty.
    enabled : Optional[bool]
        Whether the product is offered.
    family_code : Optional[str]
        That family&#039;s code, resolved here so a grid can show and group by it without a second read.
    family_id : Optional[str]
        The product&#039;s family. Null is the state that makes completeness impossible.
    id : Optional[str]
        The product&#039;s id — what a row click navigates with.
    kind : Optional[str]
        &#039;simple&#039;, &#039;model&#039; or &#039;variant&#039; — a model is a row a person should not price or sell.
    label : Optional[str]
        The resolved display name. Never empty; read `label_source` before showing it as a name.
    label_attribute : Optional[str]
        Which attribute code the name was read from, per this product&#039;s family.
    label_source : Optional[ProductLabelSource]
        Which bucket of attribute_values the name came from. &#039;sku&#039; means the catalog holds no name for this product — show that as a missing name, not as a name.
    sku : Optional[str]
        The merchant&#039;s article number.
    updated_at : Optional[str]
        When the product row was last written — the column a &quot;recently changed&quot; sort uses.
    """
    attributes: Optional[Dict[str, Any]] = Field(default=None, alias='attributes')
    completeness: Optional[Dict[str, Any]] = Field(default=None, alias='completeness')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    family_code: Optional[str] = Field(default=None, alias='family_code')
    family_id: Optional[str] = Field(default=None, alias='family_id')
    id: Optional[str] = Field(default=None, alias='id')
    kind: Optional[str] = Field(default=None, alias='kind')
    label: Optional[str] = Field(default=None, alias='label')
    label_attribute: Optional[str] = Field(default=None, alias='label_attribute')
    label_source: Optional[ProductLabelSource] = Field(default=None, alias='label_source')
    sku: Optional[str] = Field(default=None, alias='sku')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
