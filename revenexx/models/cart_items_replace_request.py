from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .cart_item_create_request import CartItemCreateRequest

T = TypeVar('T')

class CartItemsReplaceRequest(AppwriteModel, Generic[T]):
    """
    

    Attributes
    ----------
    items : List[CartItemCreateRequest[T]]
        The complete new item set (set semantics).
    """
    items: List[CartItemCreateRequest[T]] = Field(..., alias='items')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'CartItemsReplaceRequest[T]':
        """Create CartItemsReplaceRequest instance with typed data."""
        instance = cls.model_validate(data)
        if 'items' in data and data['items'] is not None:
            instance.items = [
                CartItemCreateRequest.with_data(row, model_type) 
                for row in data['items']
            ]
        return instance
