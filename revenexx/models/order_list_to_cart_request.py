from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_list_cart_mode import OrderListCartMode

class OrderListToCartRequest(AppwriteModel):
    """
    Every field is optional: with an empty body the list goes into a NEW cart for its owner, on the tenant defaults.

    Attributes
    ----------
    cart_id : Optional[str]
        Add to this existing cart. Omit to create one for the list owner and make it their current cart.
    currency : Optional[str]
        ISO 4217 code for the cart and its lines. Omit to let the carts app decide.
    mode : Optional[OrderListCartMode]
        &#039;append&#039; adds the positions (the carts app merges a line by product and price, so quantities accumulate); &#039;replace&#039; makes the list the cart&#039;s entire contents. Defaults to the tenant&#039;s &#039;cart_merge_mode&#039; setting.
    """
    cart_id: Optional[str] = Field(default=None, alias='cart_id')
    currency: Optional[str] = Field(default=None, alias='currency')
    mode: Optional[OrderListCartMode] = Field(default=None, alias='mode')
