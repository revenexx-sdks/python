from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .contact import Contact
from ..enums.registration_status import RegistrationStatus

class AuthRegisterResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    approval_required : Optional[bool]
        True when the tenant runs registration_mode=&#039;approval_required&#039; — do NOT log the buyer in.
    contact : Optional[Contact]
        The stored customer record — this app is its system of record.
    registration_status : Optional[RegistrationStatus]
        &#039;pending&#039; means the login is disabled until a merchant approves.
    user_id : Optional[str]
        The platform user that was created. Keep it: logout, /auth/me and the recovery confirm all take it.
    verification_sent : Optional[bool]
        Whether an address confirmation went out. True only when the tenant&#039;s `email_verification` asks for one on registration, the registration is a finished account rather than an application, and `verification_url` was supplied.
    welcome_sent : Optional[bool]
        Whether the tenant&#039;s welcome mail went out. Best effort on purpose: the account exists either way, and a registration is not undone because a message service was unreachable. False for an APPLICATION, which is not an account yet and is announced by `registration.submitted` instead.
    """
    approval_required: Optional[bool] = Field(default=None, alias='approval_required')
    contact: Optional[Contact] = Field(default=None, alias='contact')
    registration_status: Optional[RegistrationStatus] = Field(default=None, alias='registration_status')
    user_id: Optional[str] = Field(default=None, alias='user_id')
    verification_sent: Optional[bool] = Field(default=None, alias='verification_sent')
    welcome_sent: Optional[bool] = Field(default=None, alias='welcome_sent')
