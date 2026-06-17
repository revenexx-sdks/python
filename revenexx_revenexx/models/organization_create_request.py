from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.organization_status import OrganizationStatus

class OrganizationCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    name : str
        Company name — mirrored to the platform team.
    settings : Optional[Dict[str, Any]]
        Free-form organization settings.
    status : Optional[OrganizationStatus]
        Default &#039;active&#039;.
    vat_id : Optional[str]
        Typed model field.
    """
    name: str = Field(..., alias='name')
    settings: Optional[Dict[str, Any]] = Field(default=None, alias='settings')
    status: Optional[OrganizationStatus] = Field(default=None, alias='status')
    vat_id: Optional[str] = Field(default=None, alias='vat_id')
