from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .contact import Contact
from .contact_permissions import ContactPermissions
from .auth_session import AuthSession

class AuthOtpConfirmResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    contact : Optional[Contact]
        The customer record behind the login, or null when none is mirrored yet.
    permissions : Optional[ContactPermissions]
        A contact&#039;s effective grants, derived from its role on every read — nothing here is stored, so a role change can never leave a stale grant behind. Null when there is no contact to derive them from.
    session : Optional[AuthSession]
        Platform auth session. Treat `secret` as a credential — the trusted BFF stores it server-side (HTTP-only cookie), never in the browser.
    """
    contact: Optional[Contact] = Field(default=None, alias='contact')
    permissions: Optional[ContactPermissions] = Field(default=None, alias='permissions')
    session: Optional[AuthSession] = Field(default=None, alias='session')
