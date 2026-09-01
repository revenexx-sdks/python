from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Target(AppwriteModel):
    """
    Target

    Attributes
    ----------
    createdat : str
        Target creation time in ISO 8601 format.
    id : str
        Target ID.
    updatedat : str
        Target update date in ISO 8601 format.
    expired : bool
        Is the target expired.
    identifier : str
        The target identifier.
    name : str
        Target Name.
    providerid : Optional[str]
        Provider ID.
    providertype : str
        The target provider type. Can be one of the following: `email`, `sms` or `push`.
    userid : str
        User ID.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    updatedat: str = Field(..., alias='$updatedAt')
    expired: bool = Field(..., alias='expired')
    identifier: str = Field(..., alias='identifier')
    name: str = Field(..., alias='name')
    providerid: Optional[str] = Field(default=None, alias='providerId')
    providertype: str = Field(..., alias='providerType')
    userid: str = Field(..., alias='userId')
