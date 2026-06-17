from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.contact_role import ContactRole
from ..enums.contact_status import ContactStatus

class ContactCreateRequest(AppwriteModel):
    """
    Creates the contact (system of record) and mirrors it as a platform user (status defaults to invited).

    Attributes
    ----------
    email : str
        Typed model field.
    first_name : Optional[str]
        Typed model field.
    is_primary : Optional[bool]
        The primary contact of its organization.
    last_name : Optional[str]
        Typed model field.
    locale : Optional[str]
        BCP 47, e.g. de-DE
    organization_id : Optional[str]
        Owning organization — membership is mirrored to the platform team.
    phone : Optional[str]
        Typed model field.
    role : Optional[ContactRole]
        Default &#039;buyer&#039; — also the team role on the platform mirror.
    status : Optional[ContactStatus]
        Default &#039;invited&#039; on create.
    """
    email: str = Field(..., alias='email')
    first_name: Optional[str] = Field(default=None, alias='first_name')
    is_primary: Optional[bool] = Field(default=None, alias='is_primary')
    last_name: Optional[str] = Field(default=None, alias='last_name')
    locale: Optional[str] = Field(default=None, alias='locale')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    phone: Optional[str] = Field(default=None, alias='phone')
    role: Optional[ContactRole] = Field(default=None, alias='role')
    status: Optional[ContactStatus] = Field(default=None, alias='status')
