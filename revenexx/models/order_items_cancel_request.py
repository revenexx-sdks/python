from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .order_cancel_position import OrderCancelPosition

class OrderItemsCancelRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    cancelled_by : Optional[str]
        Who cancelled, as the caller reported it — an operator, a desk, a system. Free text; this app does not resolve it against a user directory.
    positions : List[OrderCancelPosition]
        The quantities to take off the order. Required here, unlike on /ship and /return: cancelling everything by default is not a thing anybody should be able to do by omission — that is what /cancel is for.
    reason : Optional[str]
        Why it was cancelled, free text. Mandatory when the tenant sets cancel_requires_reason — for those merchants an unexplained cancellation is refused with a 400.
    """
    cancelled_by: Optional[str] = Field(default=None, alias='cancelled_by')
    positions: List[OrderCancelPosition] = Field(..., alias='positions')
    reason: Optional[str] = Field(default=None, alias='reason')
