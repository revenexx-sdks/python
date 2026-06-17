from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthRecoveryConfirmRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    password : str
        Typed model field.
    secret : str
        Typed model field.
    user_id : str
        Typed model field.
    """
    password: str = Field(..., alias='password')
    secret: str = Field(..., alias='secret')
    user_id: str = Field(..., alias='user_id')
