from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_list_cart_mode import OrderListCartMode
from .order_list_skipped_position import OrderListSkippedPosition

class OrderListToCartResult(AppwriteModel):
    """
    

    Attributes
    ----------
    added : Optional[float]
        Positions written to the cart. Equal to the list&#039;s position count minus `skipped`.
    cart_created : Optional[bool]
        True when this call created the cart. A created cart is the owner&#039;s CURRENT cart, because a cart the buyer cannot see is not &quot;added to cart&quot;.
    cart_id : Optional[str]
        The cart the positions landed in: the one that was passed in, or the one this call created.
    list_id : Optional[str]
        The list that was converted. Unchanged by the call — a conversion reads the list, it never empties it.
    mode : Optional[OrderListCartMode]
        The mode that was actually applied — the one that was asked for, or the tenant&#039;s &#039;cart_merge_mode&#039; default when the call named none.
    skipped : Optional[List[OrderListSkippedPosition]]
        Positions left out because the catalogue no longer knows their article. Only ever non-empty when &#039;on_missing_article&#039; is &#039;skip&#039; — &#039;include&#039; converts them anyway and &#039;fail&#039; answers 400 instead.
    """
    added: Optional[float] = Field(default=None, alias='added')
    cart_created: Optional[bool] = Field(default=None, alias='cart_created')
    cart_id: Optional[str] = Field(default=None, alias='cart_id')
    list_id: Optional[str] = Field(default=None, alias='list_id')
    mode: Optional[OrderListCartMode] = Field(default=None, alias='mode')
    skipped: Optional[List[OrderListSkippedPosition]] = Field(default=None, alias='skipped')
