from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthRegisterRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    email : str
        Typed model field.
    first_name : Optional[str]
        Typed model field.
    last_name : Optional[str]
        Typed model field.
    locale : Optional[str]
        BCP 47, e.g. de-DE
    organization_id : Optional[str]
        Join an existing organization.
    organization_name : Optional[str]
        Found a new organization; the contact becomes its admin.
    password : str
        Typed model field.
    """
    email: str = Field(..., alias='email')
    first_name: Optional[str] = Field(default=None, alias='first_name')
    last_name: Optional[str] = Field(default=None, alias='last_name')
    locale: Optional[str] = Field(default=None, alias='locale')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    organization_name: Optional[str] = Field(default=None, alias='organization_name')
    password: str = Field(..., alias='password')
