from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ColumnList(AppwriteModel):
    """
    Columns List

    Attributes
    ----------
    columns : List[Any]
        List of columns.
    total : float
        Total number of columns in the given table.
    """
    columns: List[Any] = Field(..., alias='columns')
    total: float = Field(..., alias='total')
