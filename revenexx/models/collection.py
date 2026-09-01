from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .collection_field import CollectionField

T = TypeVar('T')

class Collection(AppwriteModel, Generic[T]):
    """
    A Typesense collection definition, passed through from Typesense. `name` is rewritten back to the tenant&#039;s public collection name.

    Attributes
    ----------
    default_sorting_field : Optional[str]
        Typed model field.
    enable_nested_fields : Optional[bool]
        Typed model field.
    fields : Optional[List[CollectionField[T]]]
        Typed model field.
    name : Optional[str]
        The public collection name.
    num_documents : Optional[float]
        Documents currently indexed.
    """
    default_sorting_field: Optional[str] = Field(default=None, alias='default_sorting_field')
    enable_nested_fields: Optional[bool] = Field(default=None, alias='enable_nested_fields')
    fields: Optional[List[CollectionField[T]]] = Field(default=None, alias='fields')
    name: Optional[str] = Field(default=None, alias='name')
    num_documents: Optional[float] = Field(default=None, alias='num_documents')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'Collection[T]':
        """Create Collection instance with typed data."""
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
