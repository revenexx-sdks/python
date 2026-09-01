from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Suppression(AppwriteModel):
    """
    

    Attributes
    ----------
    address : Optional[str]
        Typed model field.
    address_hash : str
        Typed model field.
    channel : str
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    expires_at : Optional[str]
        Typed model field.
    id : str
        Typed model field.
    note : Optional[str]
        Typed model field.
    reason : str
        Typed model field.
    scope : str
        Typed model field.
    source : Optional[str]
        Typed model field.
    tenant_id : str
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    address: Optional[str] = Field(..., alias='address')
    address_hash: str = Field(..., alias='address_hash')
    channel: str = Field(..., alias='channel')
    created_at: Optional[str] = Field(..., alias='created_at')
    expires_at: Optional[str] = Field(..., alias='expires_at')
    id: str = Field(..., alias='id')
    note: Optional[str] = Field(..., alias='note')
    reason: str = Field(..., alias='reason')
    scope: str = Field(..., alias='scope')
    source: Optional[str] = Field(..., alias='source')
    tenant_id: str = Field(..., alias='tenant_id')
    updated_at: Optional[str] = Field(..., alias='updated_at')
