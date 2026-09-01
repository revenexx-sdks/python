from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .order_cancellation_position import OrderCancellationPosition
from ..enums.order_cancellation_scope import OrderCancellationScope

class OrderCancellation(AppwriteModel):
    """
    A record of what was taken off an order and why — either the whole order (while nothing had shipped) or named quantities off a partly shipped one.

    Attributes
    ----------
    cancelled_by : Optional[str]
        Who cancelled, as the caller reported it — an operator, a desk, a system. Free text; this app does not resolve it against a user directory.
    created_at : Optional[str]
        When the cancellation was recorded.
    id : Optional[str]
        Primary key of the cancellation record.
    order_id : Optional[str]
        The order that was cancelled from.
    positions : Optional[List[OrderCancellationPosition]]
        What this record removed. A scope &#039;order&#039; record carries every position in full; a scope &#039;items&#039; record carries exactly the quantities that were named.
    reason : Optional[str]
        Why it was cancelled, free text. Mandatory when the tenant sets cancel_requires_reason — for those merchants an unexplained cancellation is refused with a 400.
    scope : Optional[OrderCancellationScope]
        Which of the two cancellations this was: &#039;order&#039; is the full cancel (only possible while nothing has shipped, and it cancels every position in full), &#039;items&#039; is the quantity-based one that takes open quantities off a partly shipped order.
    """
    cancelled_by: Optional[str] = Field(default=None, alias='cancelled_by')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    order_id: Optional[str] = Field(default=None, alias='order_id')
    positions: Optional[List[OrderCancellationPosition]] = Field(default=None, alias='positions')
    reason: Optional[str] = Field(default=None, alias='reason')
    scope: Optional[OrderCancellationScope] = Field(default=None, alias='scope')
