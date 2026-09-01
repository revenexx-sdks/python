from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AddressCreateRequest(AppwriteModel):
    """
    An address needs an owner: &#039;organization_id&#039; or &#039;contact_id&#039;.

    Attributes
    ----------
    city : str
        City or town.
    company : Optional[str]
        Company line on the label. Often the owning organization&#039;s name, but not always — a delivery to a construction site carries the site.
    contact_id : Optional[str]
        Owning person — a personal address only that contact uses. Exactly one of organization_id / contact_id is set.
    country : str
        ISO 3166-1 alpha-2 country code, exactly two letters. Uppercase by convention; it is what shipping and tax both key off.
    is_default : Optional[bool]
        The default address of its owner AND type: one default billing and one default shipping address per owner. Setting it moves the flag off the previous holder. Default false.
    name : Optional[str]
        Recipient line on the label — the person or department the parcel is addressed to.
    organization_id : Optional[str]
        Owning company — a company address, shared by everyone in it. Exactly one of organization_id / contact_id is set.
    phone : Optional[str]
        Phone number for the carrier to reach at this address — often a different one from the contact&#039;s own.
    region : Optional[str]
        State, province or Bundesland. Required by some destinations (US, CA), unused by most European ones.
    street : str
        Street and house number, on one line, as the local post expects it.
    street2 : Optional[str]
        The second address line: building, floor, gate, c/o. Null when there is none.
    type : Optional[str]
        What the address is FOR — one of the tenant&#039;s own address types (GET /customers/address-types), seeded with billing and shipping. A merchant may add their own (a works entrance, a central accounts office) without a release of this app. A create without it gets the type flagged as default; a type the tenant does not keep is a 400.
    zip : str
        Postal code, as text — leading zeros are real in most countries.
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
    type: Optional[str] = Field(default=None, alias='type')
    zip: str = Field(..., alias='zip')
