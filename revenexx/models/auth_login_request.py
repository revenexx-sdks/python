from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthLoginRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    email : str
        The buyer&#039;s login address — the same one the contact carries.
    password : str
        The password from registration or recovery. Wrong credentials are a 401; a correct one on an undecided application is a 403.
    """
    email: str = Field(..., alias='email')
    password: str = Field(..., alias='password')
