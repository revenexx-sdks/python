from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthSession(AppwriteModel):
    """
    Platform auth session. Treat `secret` as a credential — the trusted BFF stores it server-side (HTTP-only cookie), never in the browser.

    Attributes
    ----------
    id : Optional[str]
        The session id. Send it back as `session_id` to log out, or to have `/auth/me` check that the session is still alive.
    expire : Optional[str]
        When the session stops being valid on its own.
    provider : Optional[str]
        How the session was created. Server-minted sessions from this route are not the browser-facing email/password ones, so this says which mechanism issued it.
    secret : Optional[str]
        The session CREDENTIAL. Whoever holds it is logged in — the BFF keeps it server-side (an HTTP-only cookie), never in the browser and never in a log.
    userid : Optional[str]
        The platform user this session belongs to — the `user_id` every other auth route takes. NOT the contact id: the contact is in `contact`.
    """
    id: Optional[str] = Field(default=None, alias='$id')
    expire: Optional[str] = Field(default=None, alias='expire')
    provider: Optional[str] = Field(default=None, alias='provider')
    secret: Optional[str] = Field(default=None, alias='secret')
    userid: Optional[str] = Field(default=None, alias='userId')
