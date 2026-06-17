from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Address(AppwriteModel):
    """
    

    Attributes
    ----------
    city : Optional[str]
        Typed model field.
    company : Optional[str]
        Typed model field.
    contact_id : Optional[str]
        Typed model field.
    country : Optional[str]
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    id : Optional[str]
        Typed model field.
    is_default : Optional[bool]
        Typed model field.
    name : Optional[str]
        Typed model field.
    organization_id : Optional[str]
        Typed model field.
    phone : Optional[str]
        Typed model field.
    region : Optional[str]
        Typed model field.
    street : Optional[str]
        Typed model field.
    street2 : Optional[str]
        Typed model field.
    type : Optional[str]
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    zip : Optional[str]
        Typed model field.
    """
    city: Optional[str] = Field(default=None, alias='city')
    company: Optional[str] = Field(default=None, alias='company')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    country: Optional[str] = Field(default=None, alias='country')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    name: Optional[str] = Field(default=None, alias='name')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    phone: Optional[str] = Field(default=None, alias='phone')
    region: Optional[str] = Field(default=None, alias='region')
    street: Optional[str] = Field(default=None, alias='street')
    street2: Optional[str] = Field(default=None, alias='street2')
    type: Optional[str] = Field(default=None, alias='type')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
    zip: Optional[str] = Field(default=None, alias='zip')
