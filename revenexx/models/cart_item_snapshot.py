from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

T = TypeVar('T')

class CartItemSnapshot(AppwriteModel, Generic[T]):
    """
    The product as the buyer was shown it when this line was added — the cart&#039;s own copy, so it stays honest when the catalogue moves underneath it. Free-form apart from the price: conversion reads `unit_price` (or `price` as a fallback) and nothing else. A snapshot without a readable price leaves the line alone in both price modes, which is deliberate — a missing snapshot must never be read as &quot;free&quot;.

    Attributes
    ----------
    price : Optional[float]
        The older spelling of the same thing, read only when `unit_price` is absent.
    unit_price : Optional[float]
        The net unit price the buyer was shown. This is what carts.order books the line on under price_snapshot_mode = snapshot, and what it rewrites under = live.
    """
    price: Optional[float] = Field(default=None, alias='price')
    unit_price: Optional[float] = Field(default=None, alias='unit_price')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'CartItemSnapshot[T]':
        """Create CartItemSnapshot instance with typed data."""
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
