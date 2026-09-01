from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .health_status import HealthStatus

class HealthStatusList(AppwriteModel):
    """
    Status List

    Attributes
    ----------
    statuses : List[HealthStatus]
        List of statuses.
    total : float
        Total number of statuses that matched your query.
    """
    statuses: List[HealthStatus] = Field(..., alias='statuses')
    total: float = Field(..., alias='total')
