from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthVerificationRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    url : str
        Where the mailed link points. `userId`, `secret` and `expire` are appended as query parameters; the first two are what the confirm call takes.
    user_id : str
        The platform user whose address is being confirmed — `user_id` from the registration, or `session.userId` from a login.
    """
    url: str = Field(..., alias='url')
    user_id: str = Field(..., alias='user_id')
