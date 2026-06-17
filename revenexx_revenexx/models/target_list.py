from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .target import Target

class TargetList(AppwriteModel):
    """
    Target list

    Attributes
    ----------
    targets : List[Target]
        List of targets.
    total : float
        Total number of targets that matched your query.
    """
    targets: List[Target] = Field(..., alias='targets')
    total: float = Field(..., alias='total')
