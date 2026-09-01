from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.health_status_status import HealthStatusStatus

class HealthStatus(AppwriteModel):
    """
    Health Status

    Attributes
    ----------
    name : str
        Name of the service.
    ping : float
        Duration in milliseconds how long the health check took.
    status : HealthStatusStatus
        Service status. Possible values are: `pass`, `fail`
    """
    name: str = Field(..., alias='name')
    ping: float = Field(..., alias='ping')
    status: HealthStatusStatus = Field(..., alias='status')
