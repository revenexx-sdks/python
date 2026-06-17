from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .cart_item_create_request import CartItemCreateRequest

class CartItemsReplaceRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    items : List[CartItemCreateRequest]
        The complete new item set (set semantics).
    """
    items: List[CartItemCreateRequest] = Field(..., alias='items')
