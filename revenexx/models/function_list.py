from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .function import Function

class FunctionList(AppwriteModel):
    """
    Functions List

    Attributes
    ----------
    functions : List[Function]
        List of functions.
    total : float
        Total number of functions that matched your query.
    """
    functions: List[Function] = Field(..., alias='functions')
    total: float = Field(..., alias='total')
