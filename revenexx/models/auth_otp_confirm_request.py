from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthOtpConfirmRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    secret : str
        The one-time secret the mailed code carried. Spent on first use and expiring, so a second attempt with the same one is a 401 rather than a second session.
    user_id : str
        The `userId` the mailed code carried.
    """
    secret: str = Field(..., alias='secret')
    user_id: str = Field(..., alias='user_id')
