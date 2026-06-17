from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Identity(AppwriteModel):
    """
    Identity

    Attributes
    ----------
    createdat : str
        Identity creation date in ISO 8601 format.
    id : str
        Identity ID.
    updatedat : str
        Identity update date in ISO 8601 format.
    provider : str
        Identity Provider.
    provideraccesstoken : str
        Identity Provider Access Token.
    provideraccesstokenexpiry : str
        The date of when the access token expires in ISO 8601 format.
    provideremail : str
        Email of the User in the Identity Provider.
    providerrefreshtoken : str
        Identity Provider Refresh Token.
    provideruid : str
        ID of the User in the Identity Provider.
    userid : str
        User ID.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    updatedat: str = Field(..., alias='$updatedAt')
    provider: str = Field(..., alias='provider')
    provideraccesstoken: str = Field(..., alias='providerAccessToken')
    provideraccesstokenexpiry: str = Field(..., alias='providerAccessTokenExpiry')
    provideremail: str = Field(..., alias='providerEmail')
    providerrefreshtoken: str = Field(..., alias='providerRefreshToken')
    provideruid: str = Field(..., alias='providerUid')
    userid: str = Field(..., alias='userId')
