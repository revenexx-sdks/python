from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .page_menu_item import PageMenuItem

T = TypeVar('T')

class Menu(AppwriteModel, Generic[T]):
    """
    One navigation menu of the tenant, addressed by the stable key a theme looks it up under.

    Attributes
    ----------
    created_at : Optional[str]
        When the menu was created.
    created_by : Optional[str]
        The user id that created the menu.
    deleted_at : Optional[str]
        The tombstone. A soft-deleted menu disappears from the renderer immediately.
    id : Optional[str]
        The menu row id. Used by the management routes; the renderer addresses a menu by its `menu_key` instead, because that is the thing a theme hard-codes.
    items : Optional[List[PageMenuItem[T]]]
        The ordered navigation tree itself. Stored exactly as it was sent, so the theme and the editor agree on the shape without this app enforcing one.
    label : Optional[str]
        What this menu is called for the people who edit it. Never rendered in the storefront.
    menu_key : Optional[str]
        The stable name the theme asks for a menu by — `main`, `footer`, `account`. It is what makes seeding idempotent and what a header component looks up; renaming it detaches the menu from the theme slot.
    updated_at : Optional[str]
        When the menu was last replaced. The upsert rewrites `items` wholesale, so this is the timestamp of the whole navigation, not of one entry.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    created_by: Optional[str] = Field(default=None, alias='created_by')
    deleted_at: Optional[str] = Field(default=None, alias='deleted_at')
    id: Optional[str] = Field(default=None, alias='id')
    items: Optional[List[PageMenuItem[T]]] = Field(default=None, alias='items')
    label: Optional[str] = Field(default=None, alias='label')
    menu_key: Optional[str] = Field(default=None, alias='menu_key')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'Menu[T]':
        """Create Menu instance with typed data."""
        instance = cls.model_validate(data)
        if 'items' in data and data['items'] is not None:
            instance.items = [
                PageMenuItem.with_data(row, model_type) 
                for row in data['items']
            ]
        return instance
