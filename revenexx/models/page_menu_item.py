from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

T = TypeVar('T')

class PageMenuItem(AppwriteModel, Generic[T]):
    """
    One entry of a navigation menu. Stored verbatim, so a theme may carry extra keys of its own alongside these.

    Attributes
    ----------
    items : Optional[List[Any]]
        Sub-entries. This is how a two-level main navigation or a grouped footer is stored.
    label : Optional[str]
        The words a visitor clicks.
    to : Optional[str]
        Where the entry goes: a page slug this app serves, a path the theme routes, or an absolute URL to somewhere else.
    """
    items: Optional[List[Any]] = Field(default=None, alias='items')
    label: Optional[str] = Field(default=None, alias='label')
    to: Optional[str] = Field(default=None, alias='to')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'PageMenuItem[T]':
        """Create PageMenuItem instance with typed data."""
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
