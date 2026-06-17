from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PaymentMethod(AppwriteModel):
    """
    

    Attributes
    ----------
    code : Optional[str]
        Typed model field.
    countries : Optional[Dict[str, Any]]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    description : Optional[str]
        Typed model field.
    enabled : Optional[bool]
        Typed model field.
    fee_amount : Optional[float]
        Typed model field.
    fee_currency : Optional[str]
        Typed model field.
    fee_type : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    kind : Optional[str]
        Typed model field.
    labels : Optional[Dict[str, Any]]
        Typed model field.
    max_order_value : Optional[float]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Typed model field.
    min_order_value : Optional[float]
        Typed model field.
    name : Optional[str]
        Typed model field.
    position : Optional[float]
        Typed model field.
    provider : Optional[str]
        Typed model field.
    provider_method : Optional[str]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    code: Optional[str] = Field(default=None, alias='code')
    countries: Optional[Dict[str, Any]] = Field(default=None, alias='countries')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    description: Optional[str] = Field(default=None, alias='description')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    fee_amount: Optional[float] = Field(default=None, alias='fee_amount')
    fee_currency: Optional[str] = Field(default=None, alias='fee_currency')
    fee_type: Optional[str] = Field(default=None, alias='fee_type')
    id: Optional[str] = Field(default=None, alias='id')
    kind: Optional[str] = Field(default=None, alias='kind')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    max_order_value: Optional[float] = Field(default=None, alias='max_order_value')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    min_order_value: Optional[float] = Field(default=None, alias='min_order_value')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    provider: Optional[str] = Field(default=None, alias='provider')
    provider_method: Optional[str] = Field(default=None, alias='provider_method')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
