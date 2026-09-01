from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthMeRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    session_id : Optional[str]
        Optional session to verify. Pass it to ask &quot;is this session still alive?&quot; (a revoked one is then a 401); omit it to only ask who a user is.
    user_id : str
        The platform user to resolve — `session.userId` from the login.
    """
    session_id: Optional[str] = Field(default=None, alias='session_id')
    user_id: str = Field(..., alias='user_id')
