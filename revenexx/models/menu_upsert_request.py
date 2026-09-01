from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .page_menu_item import PageMenuItem

T = TypeVar('T')

class MenuUpsertRequest(AppwriteModel, Generic[T]):
    """
    Create or replace the menu identified by menuKey (idempotent per tenant). `items` is written wholesale — there is no per-entry edit, so send the whole tree every time.

    Attributes
    ----------
    items : Optional[List[PageMenuItem[T]]]
        The ordered navigation tree. Replaces the stored one completely.
    label : str
        What this menu is called for the people who edit it. Required on a create; an update keeps the label it had when this is left out.
    menukey : str
        The stable slot the theme asks for this menu by. Idempotency is keyed on it: sending an existing key replaces that menu instead of creating a second one.
    """
    items: Optional[List[PageMenuItem[T]]] = Field(default=None, alias='items')
    label: str = Field(..., alias='label')
    menukey: str = Field(..., alias='menuKey')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'MenuUpsertRequest[T]':
        """Create MenuUpsertRequest instance with typed data."""
        instance = cls.model_validate(data)
        if 'items' in data and data['items'] is not None:
            instance.items = [
                PageMenuItem.with_data(row, model_type) 
                for row in data['items']
            ]
        return instance
