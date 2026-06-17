from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthLogoutRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    session_id : str
        Typed model field.
    user_id : str
        Typed model field.
    """
    session_id: str = Field(..., alias='session_id')
    user_id: str = Field(..., alias='user_id')
