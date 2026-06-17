from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Greeting(AppwriteModel):
    """
    

    Attributes
    ----------
    created_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    locale : Optional[str]
        Typed model field.
    message : Optional[str]
        Typed model field.
    metadata : Optional[Dict[str, Any]]
        Typed model field.
    name : Optional[str]
        Typed model field.
    tenant_id : Optional[str]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    locale: Optional[str] = Field(default=None, alias='locale')
    message: Optional[str] = Field(default=None, alias='message')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    tenant_id: Optional[str] = Field(default=None, alias='tenant_id')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
