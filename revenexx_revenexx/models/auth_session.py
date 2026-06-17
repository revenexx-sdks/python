from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthSession(AppwriteModel):
    """
    Platform auth session. Treat `secret` as a credential — the trusted BFF stores it server-side (HTTP-only cookie), never in the browser.

    Attributes
    ----------
    id : Optional[str]
        Typed model field.
    expire : Optional[str]
        Typed model field.
    provider : Optional[str]
        Typed model field.
    secret : Optional[str]
        Typed model field.
    userid : Optional[str]
        Typed model field.
    """
    id: Optional[str] = Field(default=None, alias='$id')
    expire: Optional[str] = Field(default=None, alias='expire')
    provider: Optional[str] = Field(default=None, alias='provider')
    secret: Optional[str] = Field(default=None, alias='secret')
    userid: Optional[str] = Field(default=None, alias='userId')
