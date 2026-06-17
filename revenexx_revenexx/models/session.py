from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Session(AppwriteModel):
    """
    Session

    Attributes
    ----------
    createdat : str
        Session creation date in ISO 8601 format.
    id : str
        Session ID.
    updatedat : str
        Session update date in ISO 8601 format.
    clientcode : str
        Client code name. View list of [available options](https://github.com/appwrite/appwrite/blob/master/docs/lists/clients.json).
    clientengine : str
        Client engine name.
    clientengineversion : str
        Client engine name.
    clientname : str
        Client name.
    clienttype : str
        Client type.
    clientversion : str
        Client version.
    countrycode : str
        Country two-character ISO 3166-1 alpha code.
    countryname : str
        Country name.
    current : bool
        Returns true if this the current user session.
    devicebrand : str
        Device brand name.
    devicemodel : str
        Device model name.
    devicename : str
        Device name.
    expire : str
        Session expiration date in ISO 8601 format.
    factors : List[Any]
        Returns a list of active session factors.
    ip : str
        IP in use when the session was created.
    mfaupdatedat : str
        Most recent date in ISO 8601 format when the session successfully passed MFA challenge.
    oscode : str
        Operating system code name. View list of [available options](https://github.com/appwrite/appwrite/blob/master/docs/lists/os.json).
    osname : str
        Operating system name.
    osversion : str
        Operating system version.
    provider : str
        Session Provider.
    provideraccesstoken : str
        Session Provider Access Token.
    provideraccesstokenexpiry : str
        The date of when the access token expires in ISO 8601 format.
    providerrefreshtoken : str
        Session Provider Refresh Token.
    provideruid : str
        Session Provider User ID.
    secret : str
        Secret used to authenticate the user. Only included if the request was made with an API key
    userid : str
        User ID.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    updatedat: str = Field(..., alias='$updatedAt')
    clientcode: str = Field(..., alias='clientCode')
    clientengine: str = Field(..., alias='clientEngine')
    clientengineversion: str = Field(..., alias='clientEngineVersion')
    clientname: str = Field(..., alias='clientName')
    clienttype: str = Field(..., alias='clientType')
    clientversion: str = Field(..., alias='clientVersion')
    countrycode: str = Field(..., alias='countryCode')
    countryname: str = Field(..., alias='countryName')
    current: bool = Field(..., alias='current')
    devicebrand: str = Field(..., alias='deviceBrand')
    devicemodel: str = Field(..., alias='deviceModel')
    devicename: str = Field(..., alias='deviceName')
    expire: str = Field(..., alias='expire')
    factors: List[Any] = Field(..., alias='factors')
    ip: str = Field(..., alias='ip')
    mfaupdatedat: str = Field(..., alias='mfaUpdatedAt')
    oscode: str = Field(..., alias='osCode')
    osname: str = Field(..., alias='osName')
    osversion: str = Field(..., alias='osVersion')
    provider: str = Field(..., alias='provider')
    provideraccesstoken: str = Field(..., alias='providerAccessToken')
    provideraccesstokenexpiry: str = Field(..., alias='providerAccessTokenExpiry')
    providerrefreshtoken: str = Field(..., alias='providerRefreshToken')
    provideruid: str = Field(..., alias='providerUid')
    secret: str = Field(..., alias='secret')
    userid: str = Field(..., alias='userId')
