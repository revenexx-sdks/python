from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MfaChallenge(AppwriteModel):
    """
    MFA Challenge

    Attributes
    ----------
    createdat : str
        Token creation date in ISO 8601 format.
    id : str
        Token ID.
    expire : str
        Token expiration date in ISO 8601 format.
    userid : str
        User ID.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    expire: str = Field(..., alias='expire')
    userid: str = Field(..., alias='userId')
