from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .contact import Contact
from .contact_permissions import ContactPermissions

class AuthMeResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    contact : Optional[Contact]
        The customer record mirrored against this user, or null. A user with no contact resolves perfectly well — that is not the 404.
    permissions : Optional[ContactPermissions]
        A contact&#039;s effective grants, derived from its role on every read — nothing here is stored, so a role change can never leave a stale grant behind. Null when there is no contact to derive them from.
    user : Optional[Dict[str, Any]]
        The platform identity record, forwarded verbatim from the identity service. This app neither reshapes nor validates it, so treat unknown fields as forward-compatible; the ones named here are the ones this app itself writes and reads.
    """
    contact: Optional[Contact] = Field(default=None, alias='contact')
    permissions: Optional[ContactPermissions] = Field(default=None, alias='permissions')
    user: Optional[Dict[str, Any]] = Field(default=None, alias='user')
