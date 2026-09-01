from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .column_index import ColumnIndex

class Table(AppwriteModel):
    """
    Table

    Attributes
    ----------
    createdat : str
        Table creation date in ISO 8601 format.
    id : str
        Table ID.
    permissions : List[Any]
        Table permissions. Each entry is a permission string: an action wrapping a role, e.g. `read(&quot;any&quot;)`, `update(&quot;user:abc&quot;)`, `delete(&quot;team:abc/owner&quot;)`. Actions are `read`, `create`, `update`, `delete` and the aggregate `write` (= create + update + delete); the role inside the quotes takes the form described under “Role strings” in this document&#039;s introduction.
    updatedat : str
        Table update date in ISO 8601 format.
    bytesmax : float
        Maximum row size in bytes. Returns 0 when no limit applies.
    bytesused : float
        Currently used row size in bytes based on defined columns.
    columns : List[Any]
        Table columns.
    databaseid : str
        Database ID.
    enabled : bool
        Table enabled. Can be &#039;enabled&#039; or &#039;disabled&#039;. When disabled, the table is inaccessible to users, but remains accessible to Server SDKs using API keys.
    indexes : List[ColumnIndex]
        Table indexes.
    name : str
        Table name.
    rowsecurity : bool
        Whether row-level permissions are enabled. When it is, each record&#039;s own `$permissions` are enforced on top of the container&#039;s.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    permissions: List[Any] = Field(..., alias='$permissions')
    updatedat: str = Field(..., alias='$updatedAt')
    bytesmax: float = Field(..., alias='bytesMax')
    bytesused: float = Field(..., alias='bytesUsed')
    columns: List[Any] = Field(..., alias='columns')
    databaseid: str = Field(..., alias='databaseId')
    enabled: bool = Field(..., alias='enabled')
    indexes: List[ColumnIndex] = Field(..., alias='indexes')
    name: str = Field(..., alias='name')
    rowsecurity: bool = Field(..., alias='rowSecurity')
