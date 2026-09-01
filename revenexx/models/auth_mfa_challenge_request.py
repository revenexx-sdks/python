from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthMfaChallengeRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    factor : Optional[str]
        Which factor to challenge. Defaults to `email`, the only one this route mails.
    user_id : str
        The platform user being challenged.
    """
    factor: Optional[str] = Field(default=None, alias='factor')
    user_id: str = Field(..., alias='user_id')
