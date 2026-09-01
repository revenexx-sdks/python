from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .contact import Contact
from .contact_permissions import ContactPermissions
from .auth_session import AuthSession

class AuthLoginResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    challenge_id : Optional[str]
        The challenge to answer, when one was required. Send it back as `challenge_id`.
    contact : Optional[Contact]
        The customer record behind the login. Null when a platform user has no contact mirrored against it — a storefront should treat that as &quot;signed in, but not a customer of this app&quot;.
    mfa_required : Optional[bool]
        Present and true when the tenant&#039;s `mfa_mode` is &#039;required&#039;. The password was one of two things this buyer has to prove: a challenge has already been created and mailed, and the session above must NOT be treated as signed in until `PUT /customers/auth/mfa/challenge` confirms the code. The session travels anyway because answering needs it — the expected caller holds session material server-side, and this is the point at which that trust is used.
    permissions : Optional[ContactPermissions]
        A contact&#039;s effective grants, derived from its role on every read — nothing here is stored, so a role change can never leave a stale grant behind. Carried here so a BFF does not need a second call to decide what to render.
    session : Optional[AuthSession]
        Platform auth session. Treat `secret` as a credential — the trusted BFF stores it server-side (HTTP-only cookie), never in the browser.
    """
    challenge_id: Optional[str] = Field(default=None, alias='challenge_id')
    contact: Optional[Contact] = Field(default=None, alias='contact')
    mfa_required: Optional[bool] = Field(default=None, alias='mfa_required')
    permissions: Optional[ContactPermissions] = Field(default=None, alias='permissions')
    session: Optional[AuthSession] = Field(default=None, alias='session')
