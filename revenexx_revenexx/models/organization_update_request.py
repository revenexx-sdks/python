from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.organization_status import OrganizationStatus

class OrganizationUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value; external_team_id is mirror-managed and ignored.

    Attributes
    ----------
    name : Optional[str]
        Company name — mirrored to the platform team.
    settings : Optional[Dict[str, Any]]
        Free-form organization settings.
    status : Optional[OrganizationStatus]
        Default &#039;active&#039;.
    vat_id : Optional[str]
        Typed model field.
    """
    name: Optional[str] = Field(default=None, alias='name')
    settings: Optional[Dict[str, Any]] = Field(default=None, alias='settings')
    status: Optional[OrganizationStatus] = Field(default=None, alias='status')
    vat_id: Optional[str] = Field(default=None, alias='vat_id')
