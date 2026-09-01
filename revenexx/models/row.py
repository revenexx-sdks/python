from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

T = TypeVar('T')

class Row(AppwriteModel, Generic[T]):
    """
    Row

    Attributes
    ----------
    createdat : str
        Row creation date in ISO 8601 format.
    databaseid : str
        Database ID.
    id : str
        Row ID.
    permissions : List[Any]
        Row permissions. Each entry is a permission string: an action wrapping a role, e.g. `read(&quot;any&quot;)`, `update(&quot;user:abc&quot;)`, `delete(&quot;team:abc/owner&quot;)`. Actions are `read`, `create`, `update`, `delete` and the aggregate `write` (= create + update + delete); the role inside the quotes takes the form described under “Role strings” in this document&#039;s introduction.
    sequence : float
        Row automatically incrementing ID.
    tableid : str
        Table ID.
    updatedat : str
        Row update date in ISO 8601 format.
    """
    createdat: str = Field(..., alias='$createdAt')
    databaseid: str = Field(..., alias='$databaseId')
    id: str = Field(..., alias='$id')
    permissions: List[Any] = Field(..., alias='$permissions')
    sequence: float = Field(..., alias='$sequence')
    tableid: str = Field(..., alias='$tableId')
    updatedat: str = Field(..., alias='$updatedAt')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'Row[T]':
        """Create Row instance with typed data."""
        internal_fields = {k: v for k, v in data.items() if k.startswith('$')}
        user_data = {k: v for k, v in data.items() if not k.startswith('$')}
        instance = cls.model_validate(internal_fields)
        instance._data = model_type(**user_data) if model_type is not dict else user_data
        return instance

    _data: Any = PrivateAttr(default_factory=dict)

    @property
    def data(self) -> T:
        return cast(T, self._data)

    @data.setter
    def data(self, value: T) -> None:
        object.__setattr__(self, '_data', value)

    def to_dict(self) -> Dict[str, Any]:
        result = super().to_dict()
        if hasattr(self, '_data'):
            if isinstance(self._data, dict):
                result['data'] = self._data
            elif hasattr(self._data, 'model_dump'):
                result['data'] = self._data.model_dump(mode='json')
            else:
                result['data'] = self._data
        return result
