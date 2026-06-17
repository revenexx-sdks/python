from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PaymentProviderUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    credentials : Optional[Dict[str, Any]]
        PSP credentials — the catalog&#039;s credential_fields say which keys the auth scheme expects.
    enabled : Optional[bool]
        Only enabled providers transact (default false).
    name : Optional[str]
        Display name — defaults to the catalog label.
    options : Optional[Dict[str, Any]]
        Free-form provider options.
    provider : Optional[str]
        Provider code — must exist in the catalog (GET /payments/providers/catalog).
    test_mode : Optional[bool]
        Sandbox/test credentials (default true).
    webhook_secret : Optional[str]
        Shared secret for PSP callback verification.
    """
    credentials: Optional[Dict[str, Any]] = Field(default=None, alias='credentials')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    name: Optional[str] = Field(default=None, alias='name')
    options: Optional[Dict[str, Any]] = Field(default=None, alias='options')
    provider: Optional[str] = Field(default=None, alias='provider')
    test_mode: Optional[bool] = Field(default=None, alias='test_mode')
    webhook_secret: Optional[str] = Field(default=None, alias='webhook_secret')
