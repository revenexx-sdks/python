from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Contact(AppwriteModel):
    """
    

    Attributes
    ----------
    created_at : Optional[str]
        Typed model field.
    email : Optional[str]
        Typed model field.
    external_user_id : Optional[str]
        Typed model field.
    first_name : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    is_primary : Optional[bool]
        Typed model field.
    last_name : Optional[str]
        Typed model field.
    locale : Optional[str]
        Typed model field.
    organization_id : Optional[str]
        Typed model field.
    phone : Optional[str]
        Typed model field.
    role : Optional[str]
        Typed model field.
    status : Optional[str]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    email: Optional[str] = Field(default=None, alias='email')
    external_user_id: Optional[str] = Field(default=None, alias='external_user_id')
    first_name: Optional[str] = Field(default=None, alias='first_name')
    id: Optional[str] = Field(default=None, alias='id')
    is_primary: Optional[bool] = Field(default=None, alias='is_primary')
    last_name: Optional[str] = Field(default=None, alias='last_name')
    locale: Optional[str] = Field(default=None, alias='locale')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    phone: Optional[str] = Field(default=None, alias='phone')
    role: Optional[str] = Field(default=None, alias='role')
    status: Optional[str] = Field(default=None, alias='status')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
