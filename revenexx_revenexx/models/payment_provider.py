from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PaymentProvider(AppwriteModel):
    """
    

    Attributes
    ----------
    created_at : Optional[str]
        Typed model field.
    credentials : Optional[Dict[str, Any]]
        Typed model field.
    enabled : Optional[bool]
        Typed model field.
    id : Optional[str]
        Typed model field.
    name : Optional[str]
        Typed model field.
    options : Optional[Dict[str, Any]]
        Typed model field.
    provider : Optional[str]
        Typed model field.
    test_mode : Optional[bool]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    webhook_secret : Optional[str]
        Typed model field.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    credentials: Optional[Dict[str, Any]] = Field(default=None, alias='credentials')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    id: Optional[str] = Field(default=None, alias='id')
    name: Optional[str] = Field(default=None, alias='name')
    options: Optional[Dict[str, Any]] = Field(default=None, alias='options')
    provider: Optional[str] = Field(default=None, alias='provider')
    test_mode: Optional[bool] = Field(default=None, alias='test_mode')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
    webhook_secret: Optional[str] = Field(default=None, alias='webhook_secret')
