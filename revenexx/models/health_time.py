from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class HealthTime(AppwriteModel):
    """
    Health Time

    Attributes
    ----------
    diff : float
        Difference of unix remote and local timestamps in milliseconds.
    localtime : float
        Current unix timestamp of the core service host.
    remotetime : float
        Current unix timestamp on trustful remote server.
    """
    diff: float = Field(..., alias='diff')
    localtime: float = Field(..., alias='localTime')
    remotetime: float = Field(..., alias='remoteTime')
