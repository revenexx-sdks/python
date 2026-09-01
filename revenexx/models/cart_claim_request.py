from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.cart_merge_strategy import CartMergeStrategy

class CartClaimRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    contact_id : str
        The contact taking ownership. Every active cart of that session ends up with this contact — adopted as it stands, or folded into `target_cart_id`.
    session_key : str
        The guest session whose active carts are handed over — the key the storefront keeps in its own session or cookie and has been sending on every anonymous call. This app neither issues nor parses it, so the example shows the shape of an opaque token and not a format anything enforces.
    strategy : Optional[CartMergeStrategy]
        Override the tenant&#039;s cart_merge_strategy for this call: &#039;merge&#039; keeps the target cart&#039;s own lines, &#039;replace&#039; clears them first. Omit to use the setting.
    target_cart_id : Optional[str]
        Merge the session carts into this cart instead of adopting them.
    """
    contact_id: str = Field(..., alias='contact_id')
    session_key: str = Field(..., alias='session_key')
    strategy: Optional[CartMergeStrategy] = Field(default=None, alias='strategy')
    target_cart_id: Optional[str] = Field(default=None, alias='target_cart_id')
