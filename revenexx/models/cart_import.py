from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .cart import Cart

class CartImport(AppwriteModel):
    """
    `cart` is the cart as it now stands, totals already recomputed — the newly created one, or the target with the imported lines folded in.

    Attributes
    ----------
    cart : Optional[Cart]
        Typed model field.
    imported_lines : Optional[float]
        Lines read out of the payload. Identical product lines merge, so the cart may have gained fewer rows than this.
    """
    cart: Optional[Cart] = Field(default=None, alias='cart')
    imported_lines: Optional[float] = Field(default=None, alias='imported_lines')
