from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthLoginRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    email : str
        Typed model field.
    password : str
        Typed model field.
    """
    email: str = Field(..., alias='email')
    password: str = Field(..., alias='password')
