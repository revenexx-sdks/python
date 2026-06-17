from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CartMergeRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    source_cart_id : str
        Cart whose lines move into the target (becomes status merged).
    target_cart_id : str
        Receiving cart (must be active).
    """
    source_cart_id: str = Field(..., alias='source_cart_id')
    target_cart_id: str = Field(..., alias='target_cart_id')
