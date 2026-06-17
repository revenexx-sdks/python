from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.address_type import AddressType

class AddressCreateRequest(AppwriteModel):
    """
    An address needs an owner: &#039;organization_id&#039; or &#039;contact_id&#039;.

    Attributes
    ----------
    city : str
        Typed model field.
    company : Optional[str]
        Typed model field.
    contact_id : Optional[str]
        Owning contact (personal address).
    country : str
        ISO 3166-1 alpha-2 code.
    is_default : Optional[bool]
        The default address of its owner and type.
    name : Optional[str]
        Recipient name.
    organization_id : Optional[str]
        Owning organization (company address).
    phone : Optional[str]
        Typed model field.
    region : Optional[str]
        Typed model field.
    street : str
        Typed model field.
    street2 : Optional[str]
        Typed model field.
    type : Optional[AddressType]
        Default &#039;shipping&#039;.
    zip : str
        Typed model field.
    """
    city: str = Field(..., alias='city')
    company: Optional[str] = Field(default=None, alias='company')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    country: str = Field(..., alias='country')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    name: Optional[str] = Field(default=None, alias='name')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    phone: Optional[str] = Field(default=None, alias='phone')
    region: Optional[str] = Field(default=None, alias='region')
    street: str = Field(..., alias='street')
    street2: Optional[str] = Field(default=None, alias='street2')
    type: Optional[AddressType] = Field(default=None, alias='type')
    zip: str = Field(..., alias='zip')
