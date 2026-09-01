from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthMagicLinkRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    email : str
        Who to send the link to. An address that has never been seen creates an account rather than failing.
    url : str
        Where the mailed link points. `userId`, `secret` and `expire` are appended as query parameters; the first two are what the confirm call takes.
    """
    email: str = Field(..., alias='email')
    url: str = Field(..., alias='url')
