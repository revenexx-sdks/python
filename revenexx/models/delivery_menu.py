from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .page_menu_item import PageMenuItem

T = TypeVar('T')

class DeliveryMenu(AppwriteModel, Generic[T]):
    """
    One navigation menu, ready to render.

    Attributes
    ----------
    id : Optional[str]
        The menu KEY (`main`, `footer`, `account`), not the row id — this is the handle a theme hard-codes.
    items : Optional[List[PageMenuItem[T]]]
        The ordered navigation tree, exactly as it is stored. Render it in order; nesting is `items` inside an entry.
    label : Optional[str]
        What the menu is called for the people who edit it. A theme rarely renders it.
    """
    id: Optional[str] = Field(default=None, alias='id')
    items: Optional[List[PageMenuItem[T]]] = Field(default=None, alias='items')
    label: Optional[str] = Field(default=None, alias='label')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'DeliveryMenu[T]':
        """Create DeliveryMenu instance with typed data."""
        instance = cls.model_validate(data)
        if 'items' in data and data['items'] is not None:
            instance.items = [
                PageMenuItem.with_data(row, model_type) 
                for row in data['items']
            ]
        return instance
