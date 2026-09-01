from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

T = TypeVar('T')

class FamilyAttributesFilter(AppwriteModel, Generic[T]):
    """
    The exact-column filters this call was understood to carry, verbatim as they arrived. A query parameter that is not a column of `family_attributes` — `?status=`, a typo, a filter another entity has — is DROPPED and does not appear here, and the list comes back unfiltered. This object is the only way to tell that apart from &quot;nothing matched&quot;.

    Attributes
    ----------
    attribute_id : Optional[str]
        The literal `?attribute_id=` value this call was understood to carry.
    created_at : Optional[str]
        The literal `?created_at=` value this call was understood to carry.
    family_id : Optional[str]
        The literal `?family_id=` value this call was understood to carry.
    id : Optional[str]
        The literal `?id=` value this call was understood to carry.
    is_required : Optional[str]
        The literal `?is_required=` value this call was understood to carry.
    position : Optional[str]
        The literal `?position=` value this call was understood to carry.
    required_channels : Optional[str]
        The literal `?required_channels=` value this call was understood to carry.
    """
    attribute_id: Optional[str] = Field(default=None, alias='attribute_id')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    family_id: Optional[str] = Field(default=None, alias='family_id')
    id: Optional[str] = Field(default=None, alias='id')
    is_required: Optional[str] = Field(default=None, alias='is_required')
    position: Optional[str] = Field(default=None, alias='position')
    required_channels: Optional[str] = Field(default=None, alias='required_channels')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'FamilyAttributesFilter[T]':
        """Create FamilyAttributesFilter instance with typed data."""
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
