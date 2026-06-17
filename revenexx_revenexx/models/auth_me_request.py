from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthMeRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    session_id : Optional[str]
        Optional session to verify — answers 401 when the session is expired or revoked.
    user_id : str
        Typed model field.
    """
    session_id: Optional[str] = Field(default=None, alias='session_id')
    user_id: str = Field(..., alias='user_id')
