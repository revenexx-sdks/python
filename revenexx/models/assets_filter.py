from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

T = TypeVar('T')

class AssetsFilter(AppwriteModel, Generic[T]):
    """
    The exact-column filters this call was understood to carry, verbatim as they arrived. A query parameter that is not a column of `assets` — `?status=`, a typo, a filter another entity has — is DROPPED and does not appear here, and the list comes back unfiltered. This object is the only way to tell that apart from &quot;nothing matched&quot;.

    Attributes
    ----------
    asset_family_id : Optional[str]
        The literal `?asset_family_id=` value this call was understood to carry.
    attribute_values : Optional[str]
        The literal `?attribute_values=` value this call was understood to carry.
    code : Optional[str]
        The literal `?code=` value this call was understood to carry.
    created_at : Optional[str]
        The literal `?created_at=` value this call was understood to carry.
    delivery_path : Optional[str]
        The literal `?delivery_path=` value this call was understood to carry.
    external_url : Optional[str]
        The literal `?external_url=` value this call was understood to carry.
    id : Optional[str]
        The literal `?id=` value this call was understood to carry.
    source : Optional[str]
        The literal `?source=` value this call was understood to carry.
    storage_asset_id : Optional[str]
        The literal `?storage_asset_id=` value this call was understood to carry.
    updated_at : Optional[str]
        The literal `?updated_at=` value this call was understood to carry.
    """
    asset_family_id: Optional[str] = Field(default=None, alias='asset_family_id')
    attribute_values: Optional[str] = Field(default=None, alias='attribute_values')
    code: Optional[str] = Field(default=None, alias='code')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    delivery_path: Optional[str] = Field(default=None, alias='delivery_path')
    external_url: Optional[str] = Field(default=None, alias='external_url')
    id: Optional[str] = Field(default=None, alias='id')
    source: Optional[str] = Field(default=None, alias='source')
    storage_asset_id: Optional[str] = Field(default=None, alias='storage_asset_id')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'AssetsFilter[T]':
        """Create AssetsFilter instance with typed data."""
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
