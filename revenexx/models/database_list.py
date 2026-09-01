from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .database import Database

class DatabaseList(AppwriteModel):
    """
    Databases List

    Attributes
    ----------
    databases : List[Database]
        List of databases.
    total : float
        Total number of databases that matched your query.
    """
    databases: List[Database] = Field(..., alias='databases')
    total: float = Field(..., alias='total')
