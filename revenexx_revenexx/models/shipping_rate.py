from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ShippingRate(AppwriteModel):
    """
    

    Attributes
    ----------
    carrier : Optional[str]
        Typed model field.
    code : Optional[str]
        Typed model field.
    currency : Optional[str]
        Typed model field.
    description : Optional[str]
        Typed model field.
    eta_days_max : Optional[float]
        Typed model field.
    eta_days_min : Optional[float]
        Typed model field.
    free_reason : Optional[str]
        Typed model field.
    labels : Optional[Dict[str, Any]]
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
        Shipping method tax class (or market default).
    tax_rate : Optional[float]
        Tax rate % from markets.tax_classes for this market + tax_class.
    """
    carrier: Optional[str] = Field(default=None, alias='carrier')
    code: Optional[str] = Field(default=None, alias='code')
    currency: Optional[str] = Field(default=None, alias='currency')
    description: Optional[str] = Field(default=None, alias='description')
    eta_days_max: Optional[float] = Field(default=None, alias='eta_days_max')
    eta_days_min: Optional[float] = Field(default=None, alias='eta_days_min')
    free_reason: Optional[str] = Field(default=None, alias='free_reason')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    price: Optional[float] = Field(default=None, alias='price')
    pricing_type: Optional[str] = Field(default=None, alias='pricing_type')
    tax_class: Optional[str] = Field(default=None, alias='tax_class')
    tax_rate: Optional[float] = Field(default=None, alias='tax_rate')
