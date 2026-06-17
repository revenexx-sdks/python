from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Payment(AppwriteModel):
    """
    

    Attributes
    ----------
    amount : Optional[float]
        Typed model field.
    authorized_at : Optional[str]
        Typed model field.
    captured_at : Optional[str]
        Typed model field.
    cart_id : Optional[str]
        Typed model field.
    contact_id : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    currency : Optional[str]
        Typed model field.
    error_message : Optional[str]
        Typed model field.
    failed_at : Optional[str]
        Typed model field.
    fee_amount : Optional[float]
        Typed model field.
    id : Optional[str]
        Typed model field.
    idempotency_key : Optional[str]
        Typed model field.
    kind : Optional[str]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Typed model field.
    method_code : Optional[str]
        Typed model field.
    next_action : Optional[Dict[str, Any]]
        Typed model field.
    order_ref : Optional[str]
        Typed model field.
    provider : Optional[str]
        Typed model field.
    psp_payment_id : Optional[str]
        Typed model field.
    refunded_at : Optional[str]
        Typed model field.
    status : Optional[str]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    amount: Optional[float] = Field(default=None, alias='amount')
    authorized_at: Optional[str] = Field(default=None, alias='authorized_at')
    captured_at: Optional[str] = Field(default=None, alias='captured_at')
    cart_id: Optional[str] = Field(default=None, alias='cart_id')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    currency: Optional[str] = Field(default=None, alias='currency')
    error_message: Optional[str] = Field(default=None, alias='error_message')
    failed_at: Optional[str] = Field(default=None, alias='failed_at')
    fee_amount: Optional[float] = Field(default=None, alias='fee_amount')
    id: Optional[str] = Field(default=None, alias='id')
    idempotency_key: Optional[str] = Field(default=None, alias='idempotency_key')
    kind: Optional[str] = Field(default=None, alias='kind')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    method_code: Optional[str] = Field(default=None, alias='method_code')
    next_action: Optional[Dict[str, Any]] = Field(default=None, alias='next_action')
    order_ref: Optional[str] = Field(default=None, alias='order_ref')
    provider: Optional[str] = Field(default=None, alias='provider')
    psp_payment_id: Optional[str] = Field(default=None, alias='psp_payment_id')
    refunded_at: Optional[str] = Field(default=None, alias='refunded_at')
    status: Optional[str] = Field(default=None, alias='status')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
