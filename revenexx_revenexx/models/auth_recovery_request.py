from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthRecoveryRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    email : str
        Typed model field.
    url : str
        Redirect URL carrying userId + secret.
    """
    email: str = Field(..., alias='email')
    url: str = Field(..., alias='url')
