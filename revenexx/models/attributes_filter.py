from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

T = TypeVar('T')

class AttributesFilter(AppwriteModel, Generic[T]):
    """
    The exact-column filters this call was understood to carry, verbatim as they arrived. A query parameter that is not a column of `attributes` — `?status=`, a typo, a filter another entity has — is DROPPED and does not appear here, and the list comes back unfiltered. This object is the only way to tell that apart from &quot;nothing matched&quot;.

    Attributes
    ----------
    code : Optional[str]
        The literal `?code=` value this call was understood to carry.
    config : Optional[str]
        The literal `?config=` value this call was understood to carry.
    created_at : Optional[str]
        The literal `?created_at=` value this call was understood to carry.
    entity_ref : Optional[str]
        The literal `?entity_ref=` value this call was understood to carry.
    entity_type : Optional[str]
        The literal `?entity_type=` value this call was understood to carry.
    group_id : Optional[str]
        The literal `?group_id=` value this call was understood to carry.
    id : Optional[str]
        The literal `?id=` value this call was understood to carry.
    is_filterable : Optional[str]
        The literal `?is_filterable=` value this call was understood to carry.
    is_unique : Optional[str]
        The literal `?is_unique=` value this call was understood to carry.
    labels : Optional[str]
        The literal `?labels=` value this call was understood to carry.
    localizable : Optional[str]
        The literal `?localizable=` value this call was understood to carry.
    position : Optional[str]
        The literal `?position=` value this call was understood to carry.
    scopable : Optional[str]
        The literal `?scopable=` value this call was understood to carry.
    type : Optional[str]
        The literal `?type=` value this call was understood to carry.
    updated_at : Optional[str]
        The literal `?updated_at=` value this call was understood to carry.
    usable_in_grid : Optional[str]
        The literal `?usable_in_grid=` value this call was understood to carry.
    validation : Optional[str]
        The literal `?validation=` value this call was understood to carry.
    """
    code: Optional[str] = Field(default=None, alias='code')
    config: Optional[str] = Field(default=None, alias='config')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    entity_ref: Optional[str] = Field(default=None, alias='entity_ref')
    entity_type: Optional[str] = Field(default=None, alias='entity_type')
    group_id: Optional[str] = Field(default=None, alias='group_id')
    id: Optional[str] = Field(default=None, alias='id')
    is_filterable: Optional[str] = Field(default=None, alias='is_filterable')
    is_unique: Optional[str] = Field(default=None, alias='is_unique')
    labels: Optional[str] = Field(default=None, alias='labels')
    localizable: Optional[str] = Field(default=None, alias='localizable')
    position: Optional[str] = Field(default=None, alias='position')
    scopable: Optional[str] = Field(default=None, alias='scopable')
    type: Optional[str] = Field(default=None, alias='type')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
    usable_in_grid: Optional[str] = Field(default=None, alias='usable_in_grid')
    validation: Optional[str] = Field(default=None, alias='validation')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'AttributesFilter[T]':
        """Create AttributesFilter instance with typed data."""
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
