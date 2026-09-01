from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Topic(AppwriteModel):
    """
    Topic

    Attributes
    ----------
    createdat : str
        Topic creation time in ISO 8601 format.
    id : str
        Topic ID.
    updatedat : str
        Topic update date in ISO 8601 format.
    emailtotal : float
        Total count of email subscribers subscribed to the topic.
    name : str
        The name of the topic.
    pushtotal : float
        Total count of push subscribers subscribed to the topic.
    smstotal : float
        Total count of SMS subscribers subscribed to the topic.
    subscribe : List[Any]
        Subscribe permissions.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    updatedat: str = Field(..., alias='$updatedAt')
    emailtotal: float = Field(..., alias='emailTotal')
    name: str = Field(..., alias='name')
    pushtotal: float = Field(..., alias='pushTotal')
    smstotal: float = Field(..., alias='smsTotal')
    subscribe: List[Any] = Field(..., alias='subscribe')
