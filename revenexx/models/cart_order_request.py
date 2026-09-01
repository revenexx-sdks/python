from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CartOrderRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    order_ref : Optional[str]
        The order number this cart becomes, in order management&#039;s own numbering. Stored on the cart — filtering on it is how anyone gets from an order back to the cart behind it — and it is also the reference the stock reservation is booked under. Omit it and the cart id is used for the reservation instead.
    """
    order_ref: Optional[str] = Field(default=None, alias='order_ref')
