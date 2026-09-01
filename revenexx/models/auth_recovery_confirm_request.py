from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthRecoveryConfirmRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    password : str
        The new password. It replaces the old one immediately; existing sessions are the identity service&#039;s business, not this app&#039;s.
    secret : str
        The one-time secret from the mailed link. Only that value works — it is spent on first use and expires, and anything else is a 401, so no example here would be anything but a call that fails.
    user_id : str
        The `userId` the mailed link carried.
    """
    password: str = Field(..., alias='password')
    secret: str = Field(..., alias='secret')
    user_id: str = Field(..., alias='user_id')
