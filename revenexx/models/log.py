from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Log(AppwriteModel):
    """
    Log

    Attributes
    ----------
    clientcode : str
        Client code name. A short code such as `CH` for Chrome, derived from the request&#039;s User-Agent by the core service; the full code list is not part of this API.
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
    devicebrand : str
        Device brand name.
    devicemodel : str
        Device model name.
    devicename : str
        Device name.
    event : str
        Event name.
    ip : str
        IP session in use when the session was created.
    mode : str
        API mode when event triggered.
    oscode : str
        Operating system code name. A short code such as `AND` for Android, derived from the request&#039;s User-Agent by the core service; the full code list is not part of this API.
    osname : str
        Operating system name.
    osversion : str
        Operating system version.
    time : str
        Log creation date in ISO 8601 format.
    useremail : str
        User Email.
    userid : str
        User ID.
    username : str
        User Name.
    """
    clientcode: str = Field(..., alias='clientCode')
    clientengine: str = Field(..., alias='clientEngine')
    clientengineversion: str = Field(..., alias='clientEngineVersion')
    clientname: str = Field(..., alias='clientName')
    clienttype: str = Field(..., alias='clientType')
    clientversion: str = Field(..., alias='clientVersion')
    countrycode: str = Field(..., alias='countryCode')
    countryname: str = Field(..., alias='countryName')
    devicebrand: str = Field(..., alias='deviceBrand')
    devicemodel: str = Field(..., alias='deviceModel')
    devicename: str = Field(..., alias='deviceName')
    event: str = Field(..., alias='event')
    ip: str = Field(..., alias='ip')
    mode: str = Field(..., alias='mode')
    oscode: str = Field(..., alias='osCode')
    osname: str = Field(..., alias='osName')
    osversion: str = Field(..., alias='osVersion')
    time: str = Field(..., alias='time')
    useremail: str = Field(..., alias='userEmail')
    userid: str = Field(..., alias='userId')
    username: str = Field(..., alias='userName')
