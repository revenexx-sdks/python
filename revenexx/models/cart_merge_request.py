from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CartMergeRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    source_cart_id : str
        The cart being folded in. It must be active, and it does NOT survive as a workspace: its lines are copied into the target, it becomes status merged, and merged_into_cart_id points at the target. Its own lines stay on it as the record of what was moved.
    target_cart_id : str
        The cart that SURVIVES. Must be active; it gains the source&#039;s lines (identical product lines at the same price adding up) and its totals are recomputed.
    """
    source_cart_id: str = Field(..., alias='source_cart_id')
    target_cart_id: str = Field(..., alias='target_cart_id')
