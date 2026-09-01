from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Membership(AppwriteModel):
    """
    Membership

    Attributes
    ----------
    createdat : str
        Membership creation date in ISO 8601 format.
    id : str
        Membership ID.
    updatedat : str
        Membership update date in ISO 8601 format.
    confirm : bool
        User confirmation status, true if the user has joined the team or false otherwise.
    invited : str
        Date, the user has been invited to join the team in ISO 8601 format.
    joined : str
        Date, the user has accepted the invitation to join the team in ISO 8601 format.
    mfa : bool
        Multi factor authentication status, true if the user has MFA enabled or false otherwise. Hide this attribute by toggling membership privacy in the Console.
    roles : List[Any]
        User list of roles
    teamid : str
        Team ID.
    teamname : str
        Team name.
    useremail : str
        User email address. Hide this attribute by toggling membership privacy in the Console.
    userid : str
        User ID.
    username : str
        User name. Hide this attribute by toggling membership privacy in the Console.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    updatedat: str = Field(..., alias='$updatedAt')
    confirm: bool = Field(..., alias='confirm')
    invited: str = Field(..., alias='invited')
    joined: str = Field(..., alias='joined')
    mfa: bool = Field(..., alias='mfa')
    roles: List[Any] = Field(..., alias='roles')
    teamid: str = Field(..., alias='teamId')
    teamname: str = Field(..., alias='teamName')
    useremail: str = Field(..., alias='userEmail')
    userid: str = Field(..., alias='userId')
    username: str = Field(..., alias='userName')
