from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .execution import Execution

class ExecutionList(AppwriteModel):
    """
    Executions List

    Attributes
    ----------
    executions : List[Execution]
        List of executions.
    total : float
        Total number of executions that matched your query.
    """
    executions: List[Execution] = Field(..., alias='executions')
    total: float = Field(..., alias='total')
