from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .target import Target

class Subscriber(AppwriteModel):
    """
    Subscriber

    Attributes
    ----------
    createdat : str
        Subscriber creation time in ISO 8601 format.
    id : str
        Subscriber ID.
    updatedat : str
        Subscriber update date in ISO 8601 format.
    providertype : str
        The target provider type. Can be one of the following: `email`, `sms` or `push`.
    target : Target
        Target.
    targetid : str
        Target ID.
    topicid : str
        Topic ID.
    userid : str
        Topic ID.
    username : str
        User Name.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    updatedat: str = Field(..., alias='$updatedAt')
    providertype: str = Field(..., alias='providerType')
    target: Target = Field(..., alias='target')
    targetid: str = Field(..., alias='targetId')
    topicid: str = Field(..., alias='topicId')
    userid: str = Field(..., alias='userId')
    username: str = Field(..., alias='userName')
