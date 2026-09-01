from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .index import Index

class Collection2(AppwriteModel):
    """
    Collection

    Attributes
    ----------
    createdat : str
        Collection creation date in ISO 8601 format.
    id : str
        Collection ID.
    permissions : List[Any]
        Collection permissions. Each entry is a permission string: an action wrapping a role, e.g. `read(&quot;any&quot;)`, `update(&quot;user:abc&quot;)`, `delete(&quot;team:abc/owner&quot;)`. Actions are `read`, `create`, `update`, `delete` and the aggregate `write` (= create + update + delete); the role inside the quotes takes the form described under “Role strings” in this document&#039;s introduction.
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
        Whether document-level permissions are enabled. When it is, each record&#039;s own `$permissions` are enforced on top of the container&#039;s.
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
