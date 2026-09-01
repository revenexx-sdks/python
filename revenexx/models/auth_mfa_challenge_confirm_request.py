from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthMfaChallengeConfirmRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    challenge_id : str
        The `$id` the send answered with.
    code : str
        What the buyer typed.
    session_secret : str
        The same session the challenge was created with.
    user_id : Optional[str]
        The platform user, for the caller&#039;s own bookkeeping. The challenge already knows whose it is.
    """
    challenge_id: str = Field(..., alias='challenge_id')
    code: str = Field(..., alias='code')
    session_secret: str = Field(..., alias='session_secret')
    user_id: Optional[str] = Field(default=None, alias='user_id')
