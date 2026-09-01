from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

T = TypeVar('T')

class ProductAssociationsFilter(AppwriteModel, Generic[T]):
    """
    The exact-column filters this call was understood to carry, verbatim as they arrived. A query parameter that is not a column of `product_associations` — `?status=`, a typo, a filter another entity has — is DROPPED and does not appear here, and the list comes back unfiltered. This object is the only way to tell that apart from &quot;nothing matched&quot;.

    Attributes
    ----------
    association_type_id : Optional[str]
        The literal `?association_type_id=` value this call was understood to carry.
    created_at : Optional[str]
        The literal `?created_at=` value this call was understood to carry.
    id : Optional[str]
        The literal `?id=` value this call was understood to carry.
    position : Optional[str]
        The literal `?position=` value this call was understood to carry.
    product_id : Optional[str]
        The literal `?product_id=` value this call was understood to carry.
    quantity : Optional[str]
        The literal `?quantity=` value this call was understood to carry.
    target_product_id : Optional[str]
        The literal `?target_product_id=` value this call was understood to carry.
    """
    association_type_id: Optional[str] = Field(default=None, alias='association_type_id')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    position: Optional[str] = Field(default=None, alias='position')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    quantity: Optional[str] = Field(default=None, alias='quantity')
    target_product_id: Optional[str] = Field(default=None, alias='target_product_id')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'ProductAssociationsFilter[T]':
        """Create ProductAssociationsFilter instance with typed data."""
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
