from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ChannelVisibilityItem(AppwriteModel):
    """
    

    Attributes
    ----------
    channels : Optional[List[Any]]
        The row&#039;s channel scope slugs. Empty or absent means unassigned — the case the policy decides.
    id : str
        The row id, echoed back on the decision. Opaque to this app — it is never looked up, so any non-empty string is accepted and nothing has to exist. In practice it is the entity id POST /api/v1/scopes/lookup answered with, which is what the example shows.
    """
    channels: Optional[List[Any]] = Field(default=None, alias='channels')
    id: str = Field(..., alias='id')
