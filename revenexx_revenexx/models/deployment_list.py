from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .deployment import Deployment

class DeploymentList(AppwriteModel):
    """
    Deployments List

    Attributes
    ----------
    deployments : List[Deployment]
        List of deployments.
    total : float
        Total number of deployments that matched your query.
    """
    deployments: List[Deployment] = Field(..., alias='deployments')
    total: float = Field(..., alias='total')
