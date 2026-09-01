from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthLogoutRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    session_id : str
        The session to revoke — `session.$id` from the login.
    user_id : str
        The platform user — `session.userId` from the login.
    """
    session_id: str = Field(..., alias='session_id')
    user_id: str = Field(..., alias='user_id')
