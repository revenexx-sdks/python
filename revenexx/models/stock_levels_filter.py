from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

T = TypeVar('T')

class StockLevelsFilter(AppwriteModel, Generic[T]):
    """
    The exact-column filters this call was understood to carry, verbatim as they arrived. A query parameter that is not a column of `stock_levels` — a typo, a filter another entity has, `?q=` — is DROPPED and cannot appear here, and the list comes back unfiltered. This object is the only way to tell that apart from &quot;nothing matched&quot;.

    Attributes
    ----------
    created_at : Optional[str]
        The literal `?created_at=` value this call was understood to carry.
    id : Optional[str]
        The literal `?id=` value this call was understood to carry.
    location_id : Optional[str]
        The literal `?location_id=` value this call was understood to carry.
    metadata : Optional[str]
        The literal `?metadata=` value this call was understood to carry.
    on_hand : Optional[str]
        The literal `?on_hand=` value this call was understood to carry.
    product_id : Optional[str]
        The literal `?product_id=` value this call was understood to carry.
    reorder_point : Optional[str]
        The literal `?reorder_point=` value this call was understood to carry.
    reserved : Optional[str]
        The literal `?reserved=` value this call was understood to carry.
    sku : Optional[str]
        The literal `?sku=` value this call was understood to carry.
    updated_at : Optional[str]
        The literal `?updated_at=` value this call was understood to carry.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    location_id: Optional[str] = Field(default=None, alias='location_id')
    metadata: Optional[str] = Field(default=None, alias='metadata')
    on_hand: Optional[str] = Field(default=None, alias='on_hand')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    reorder_point: Optional[str] = Field(default=None, alias='reorder_point')
    reserved: Optional[str] = Field(default=None, alias='reserved')
    sku: Optional[str] = Field(default=None, alias='sku')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'StockLevelsFilter[T]':
        """Create StockLevelsFilter instance with typed data."""
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
