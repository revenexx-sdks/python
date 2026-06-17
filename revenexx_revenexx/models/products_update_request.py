from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ProductsUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    attribute_values : Optional[Dict[str, Any]]
        Typed model field.
    completeness : Optional[Dict[str, Any]]
        Typed model field.
    deleted_at : Optional[str]
        Typed model field.
    enabled : Optional[bool]
        Typed model field.
    family_id : Optional[str]
        Typed model field.
    family_variant_id : Optional[str]
        Typed model field.
    kind : Optional[str]
        Typed model field.
    parent_id : Optional[str]
        Typed model field.
    quantified_associations : Optional[Dict[str, Any]]
        Typed model field.
    sku : Optional[str]
        Typed model field.
    tax_class : Optional[str]
        Typed model field.
    """
    attribute_values: Optional[Dict[str, Any]] = Field(default=None, alias='attribute_values')
    completeness: Optional[Dict[str, Any]] = Field(default=None, alias='completeness')
    deleted_at: Optional[str] = Field(default=None, alias='deleted_at')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    family_id: Optional[str] = Field(default=None, alias='family_id')
    family_variant_id: Optional[str] = Field(default=None, alias='family_variant_id')
    kind: Optional[str] = Field(default=None, alias='kind')
    parent_id: Optional[str] = Field(default=None, alias='parent_id')
    quantified_associations: Optional[Dict[str, Any]] = Field(default=None, alias='quantified_associations')
    sku: Optional[str] = Field(default=None, alias='sku')
    tax_class: Optional[str] = Field(default=None, alias='tax_class')
