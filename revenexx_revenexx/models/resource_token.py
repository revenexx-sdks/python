from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ResourceToken(AppwriteModel):
    """
    ResourceToken

    Attributes
    ----------
    createdat : str
        Token creation date in ISO 8601 format.
    id : str
        Token ID.
    accessedat : str
        Most recent access date in ISO 8601 format. This attribute is only updated again after 24 hours.
    expire : str
        Token expiration date in ISO 8601 format.
    resourceid : str
        Resource ID.
    resourcetype : str
        Resource type.
    secret : str
        JWT encoded string.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    accessedat: str = Field(..., alias='accessedAt')
    expire: str = Field(..., alias='expire')
    resourceid: str = Field(..., alias='resourceId')
    resourcetype: str = Field(..., alias='resourceType')
    secret: str = Field(..., alias='secret')
