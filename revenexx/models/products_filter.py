from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

T = TypeVar('T')

class ProductsFilter(AppwriteModel, Generic[T]):
    """
    The exact-column filters this call was understood to carry, verbatim as they arrived. A query parameter that is not a column of `products` — `?status=`, a typo, a filter another entity has — is DROPPED and does not appear here, and the list comes back unfiltered. This object is the only way to tell that apart from &quot;nothing matched&quot;.

    Attributes
    ----------
    attribute_values : Optional[str]
        The literal `?attribute_values=` value this call was understood to carry.
    completeness : Optional[str]
        The literal `?completeness=` value this call was understood to carry.
    created_at : Optional[str]
        The literal `?created_at=` value this call was understood to carry.
    deleted_at : Optional[str]
        The literal `?deleted_at=` value this call was understood to carry.
    enabled : Optional[str]
        The literal `?enabled=` value this call was understood to carry.
    family_id : Optional[str]
        The literal `?family_id=` value this call was understood to carry.
    family_variant_id : Optional[str]
        The literal `?family_variant_id=` value this call was understood to carry.
    id : Optional[str]
        The literal `?id=` value this call was understood to carry.
    kind : Optional[str]
        The literal `?kind=` value this call was understood to carry.
    label : Optional[str]
        The literal `?label=` value this call was understood to carry.
    parent_id : Optional[str]
        The literal `?parent_id=` value this call was understood to carry.
    quantified_associations : Optional[str]
        The literal `?quantified_associations=` value this call was understood to carry.
    sku : Optional[str]
        The literal `?sku=` value this call was understood to carry.
    tax_class : Optional[str]
        The literal `?tax_class=` value this call was understood to carry.
    updated_at : Optional[str]
        The literal `?updated_at=` value this call was understood to carry.
    """
    attribute_values: Optional[str] = Field(default=None, alias='attribute_values')
    completeness: Optional[str] = Field(default=None, alias='completeness')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    deleted_at: Optional[str] = Field(default=None, alias='deleted_at')
    enabled: Optional[str] = Field(default=None, alias='enabled')
    family_id: Optional[str] = Field(default=None, alias='family_id')
    family_variant_id: Optional[str] = Field(default=None, alias='family_variant_id')
    id: Optional[str] = Field(default=None, alias='id')
    kind: Optional[str] = Field(default=None, alias='kind')
    label: Optional[str] = Field(default=None, alias='label')
    parent_id: Optional[str] = Field(default=None, alias='parent_id')
    quantified_associations: Optional[str] = Field(default=None, alias='quantified_associations')
    sku: Optional[str] = Field(default=None, alias='sku')
    tax_class: Optional[str] = Field(default=None, alias='tax_class')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'ProductsFilter[T]':
        """Create ProductsFilter instance with typed data."""
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
