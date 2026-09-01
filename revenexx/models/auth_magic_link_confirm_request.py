from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthMagicLinkConfirmRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    secret : str
        The one-time secret the mailed link carried. Spent on first use and expiring, so a second attempt with the same one is a 401 rather than a second session.
    user_id : str
        The `userId` the mailed link carried.
    """
    secret: str = Field(..., alias='secret')
    user_id: str = Field(..., alias='user_id')
