from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_payment_status import OrderPaymentStatus

class OrderPaymentStatusUpdateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    payment_id : Optional[str]
        The reference into the payment system. MERGED into the order&#039;s payment snapshot under &#039;payment_id&#039; — the rest of the snapshot is left alone — and carried in the order.payment_status.changed event. Omitted leaves the snapshot untouched.
    status : OrderPaymentStatus
        The new value of the payment dimension. Whether the order is PAID, and the dimension this app does not decide: it is fed from outside through POST /orders/{id}/payment-status (the payments app or an ERP), and only seeded at place-time from payment.status. Orthogonal to the lifecycle — a completed order can still be open, and a paid one can still be pending.
    """
    payment_id: Optional[str] = Field(default=None, alias='payment_id')
    status: OrderPaymentStatus = Field(..., alias='status')
