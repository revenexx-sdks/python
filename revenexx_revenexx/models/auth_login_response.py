from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .contact import Contact
from .auth_session import AuthSession

class AuthLoginResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    contact : Optional[Contact]
        Typed model field.
    session : Optional[AuthSession]
        Typed model field.
    """
    contact: Optional[Contact] = Field(default=None, alias='contact')
    session: Optional[AuthSession] = Field(default=None, alias='session')
