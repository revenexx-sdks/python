from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ContactInviteRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    invited_by : Optional[str]
        Who did the inviting, as the recipient should read it. Absent, the company name is used — &quot;Beispiel GmbH invited you&quot; reads better than the name of somebody they have never heard of.
    url : str
        Where the invitation points — the storefront sign-in, normally. There is no token in it: the person is already a member and only has to sign in.
    """
    invited_by: Optional[str] = Field(default=None, alias='invited_by')
    url: str = Field(..., alias='url')
