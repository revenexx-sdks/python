from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .order_list_item_input import OrderListItemInput

class OrderListItemsReplaceRequest(AppwriteModel):
    """
    Replace ALL positions of the list (set semantics).

    Attributes
    ----------
    items : List[OrderListItemInput]
        The new full set of positions, in the order they should carry. An empty array empties the list. Every existing position is deleted and rewritten, so ids are NOT preserved. The array order is the DEFAULT and not an override: an entry that names no `position` takes its index, one that names its own keeps it — so a replace does not by itself renumber the list from zero.
    """
    items: List[OrderListItemInput] = Field(..., alias='items')
