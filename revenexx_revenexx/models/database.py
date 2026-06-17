from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.database_type import DatabaseType

class Database(AppwriteModel):
    """
    Database

    Attributes
    ----------
    createdat : str
        Database creation date in ISO 8601 format.
    id : str
        Database ID.
    updatedat : str
        Database update date in ISO 8601 format.
    enabled : bool
        If database is enabled. Can be &#039;enabled&#039; or &#039;disabled&#039;. When disabled, the database is inaccessible to users, but remains accessible to Server SDKs using API keys.
    name : str
        Database name.
    type : DatabaseType
        Database type.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    updatedat: str = Field(..., alias='$updatedAt')
    enabled: bool = Field(..., alias='enabled')
    name: str = Field(..., alias='name')
    type: DatabaseType = Field(..., alias='type')
