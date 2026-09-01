from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderListToOrderRequest(AppwriteModel):
    """
    Every field is optional — the buyer, the organization and the positions all come from the list.

    Attributes
    ----------
    currency : Optional[str]
        ISO 4217 code. Omit to let the orders app apply the market default.
    customer_order_number : Optional[str]
        The BUYER&#039;s own order or purchase-order number, forwarded to the orders app verbatim. Free text and never generated here: it exists so the paperwork can carry the number the buyer&#039;s accounts payable will look for.
    """
    currency: Optional[str] = Field(default=None, alias='currency')
    customer_order_number: Optional[str] = Field(default=None, alias='customer_order_number')
