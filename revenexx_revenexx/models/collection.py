from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .index import Index

class Collection(AppwriteModel):
    """
    Collection

    Attributes
    ----------
    createdat : str
        Collection creation date in ISO 8601 format.
    id : str
        Collection ID.
    permissions : List[Any]
        Collection permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
    updatedat : str
        Collection update date in ISO 8601 format.
    attributes : List[Any]
        Collection attributes.
    bytesmax : float
        Maximum document size in bytes. Returns 0 when no limit applies.
    bytesused : float
        Currently used document size in bytes based on defined attributes.
    databaseid : str
        Database ID.
    documentsecurity : bool
        Whether document-level permissions are enabled. [Learn more about permissions](https://appwrite.io/docs/permissions).
    enabled : bool
        Collection enabled. Can be &#039;enabled&#039; or &#039;disabled&#039;. When disabled, the collection is inaccessible to users, but remains accessible to Server SDKs using API keys.
    indexes : List[Index]
        Collection indexes.
    name : str
        Collection name.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    permissions: List[Any] = Field(..., alias='$permissions')
    updatedat: str = Field(..., alias='$updatedAt')
    attributes: List[Any] = Field(..., alias='attributes')
    bytesmax: float = Field(..., alias='bytesMax')
    bytesused: float = Field(..., alias='bytesUsed')
    databaseid: str = Field(..., alias='databaseId')
    documentsecurity: bool = Field(..., alias='documentSecurity')
    enabled: bool = Field(..., alias='enabled')
    indexes: List[Index] = Field(..., alias='indexes')
    name: str = Field(..., alias='name')
