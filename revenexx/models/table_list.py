from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .table import Table

class TableList(AppwriteModel):
    """
    Tables List

    Attributes
    ----------
    tables : List[Table]
        List of tables.
    total : float
        Total number of tables that matched your query.
    """
    tables: List[Table] = Field(..., alias='tables')
    total: float = Field(..., alias='total')
