from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_payment_status import OrderPaymentStatus

class OrderPaymentStatusUpdateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    payment_id : Optional[str]
        Reference into the payment system — merged into the order&#039;s payment snapshot.
    status : OrderPaymentStatus
        The new payment dimension value.
    """
    payment_id: Optional[str] = Field(default=None, alias='payment_id')
    status: OrderPaymentStatus = Field(..., alias='status')
