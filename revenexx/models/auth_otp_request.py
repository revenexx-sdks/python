from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthOtpRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    email : str
        Who to send the code to. As with the sign-in link, an unknown address creates an account rather than failing.
    """
    email: str = Field(..., alias='email')
