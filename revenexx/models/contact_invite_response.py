from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ContactInviteResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    contact_id : Optional[str]
        Who was invited.
    invited : Optional[bool]
        Always true when this answers — a failure to send is a 502, not a false here.
    organization_id : Optional[str]
        The company they were invited into.
    """
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    invited: Optional[bool] = Field(default=None, alias='invited')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
