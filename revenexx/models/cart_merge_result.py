from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .cart import Cart

class CartMergeResult(AppwriteModel):
    """
    Which cart survived, and what it cost. `target` is the cart that SURVIVES, already recomputed — that is the one to render. The source cart still exists and still holds its own lines: a merge copies them into the target and closes the source, it does not move them.

    Attributes
    ----------
    merged_cart_id : Optional[str]
        The source cart, now status merged, with merged_into_cart_id pointing at the target. It still exists and still holds its own lines: the merge copies, it does not move.
    merged_lines : Optional[float]
        Lines read out of the source. Identical product lines at the same price add up rather than duplicating, so the target may have gained fewer rows than this.
    target : Optional[Cart]
        Typed model field.
    """
    merged_cart_id: Optional[str] = Field(default=None, alias='merged_cart_id')
    merged_lines: Optional[float] = Field(default=None, alias='merged_lines')
    target: Optional[Cart] = Field(default=None, alias='target')
