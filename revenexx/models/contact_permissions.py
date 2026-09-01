from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.contact_permissions_permissions import ContactPermissionsPermissions

class ContactPermissions(AppwriteModel):
    """
    A contact&#039;s effective grants, derived from its role on every read — nothing here is stored, so a role change can never leave a stale grant behind. Carried here so a BFF does not need a second call to decide what to render.

    Attributes
    ----------
    active : Optional[bool]
        False while the contact is blocked or its registration is still pending/rejected — it holds the role but must not act on it.
    contact_id : Optional[str]
        The person these grants belong to. Null when the answer describes nobody — a user with no contact mirrored against it.
    order_approval_limit : Optional[float]
        Amount ceiling in the market&#039;s currency; null means no ceiling. Only meaningful together with the &#039;orders.approve&#039; permission.
    organization_id : Optional[str]
        The organization the role applies inside. Null for a standalone (B2C) contact — a role with no company to hold it in.
    permissions : Optional[List[ContactPermissionsPermissions]]
        What this role may do. Derived from the role — see GET /customers/roles.
    role : Optional[str]
        The role this contact holds in its organization, and the only input to `permissions`.
    """
    active: Optional[bool] = Field(default=None, alias='active')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    order_approval_limit: Optional[float] = Field(default=None, alias='order_approval_limit')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    permissions: Optional[List[ContactPermissionsPermissions]] = Field(default=None, alias='permissions')
    role: Optional[str] = Field(default=None, alias='role')
