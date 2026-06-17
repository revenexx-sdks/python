from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ShippingMethod(AppwriteModel):
    """
    

    Attributes
    ----------
    carrier : Optional[str]
        Typed model field.
    code : Optional[str]
        Typed model field.
    countries : Optional[Dict[str, Any]]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    currency : Optional[str]
        Typed model field.
    description : Optional[str]
        Typed model field.
    enabled : Optional[bool]
        Typed model field.
    eta_days_max : Optional[float]
        Typed model field.
    eta_days_min : Optional[float]
        Typed model field.
    free_above : Optional[float]
        Typed model field.
    id : Optional[str]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    matrix_attribute : Optional[str]
        Typed model field.
    matrix_basis : Optional[str]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Typed model field.
    name : Optional[str]
        Typed model field.
    position : Optional[float]
        Typed model field.
    price : Optional[float]
        Typed model field.
    pricing_type : Optional[str]
        Typed model field.
    tax_class : Optional[str]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    carrier: Optional[str] = Field(default=None, alias='carrier')
    code: Optional[str] = Field(default=None, alias='code')
    countries: Optional[Dict[str, Any]] = Field(default=None, alias='countries')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    currency: Optional[str] = Field(default=None, alias='currency')
    description: Optional[str] = Field(default=None, alias='description')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    eta_days_max: Optional[float] = Field(default=None, alias='eta_days_max')
    eta_days_min: Optional[float] = Field(default=None, alias='eta_days_min')
    free_above: Optional[float] = Field(default=None, alias='free_above')
    id: Optional[str] = Field(default=None, alias='id')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    matrix_attribute: Optional[str] = Field(default=None, alias='matrix_attribute')
    matrix_basis: Optional[str] = Field(default=None, alias='matrix_basis')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    price: Optional[float] = Field(default=None, alias='price')
    pricing_type: Optional[str] = Field(default=None, alias='pricing_type')
    tax_class: Optional[str] = Field(default=None, alias='tax_class')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
