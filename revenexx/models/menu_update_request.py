from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .page_menu_item import PageMenuItem

T = TypeVar('T')

class MenuUpdateRequest(AppwriteModel, Generic[T]):
    """
    Partial update — omitted fields keep their current value. `items` is replaced wholesale when sent.

    Attributes
    ----------
    items : Optional[List[PageMenuItem[T]]]
        The ordered navigation tree. Replaces the stored one completely.
    label : Optional[str]
        What this menu is called for the people who edit it.
    """
    items: Optional[List[PageMenuItem[T]]] = Field(default=None, alias='items')
    label: Optional[str] = Field(default=None, alias='label')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'MenuUpdateRequest[T]':
        """Create MenuUpdateRequest instance with typed data."""
        instance = cls.model_validate(data)
        if 'items' in data and data['items'] is not None:
            instance.items = [
                PageMenuItem.with_data(row, model_type) 
                for row in data['items']
            ]
        return instance
