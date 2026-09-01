from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class StockLevelAdjustRequest(AppwriteModel):
    """
    Correct ONE stock row. The row already knows its location and its item, so a caller owes only the signed delta and a reason — which is exactly what an operator can be asked for in a dialog.

    Attributes
    ----------
    quantity : float
        The SIGNED correction to this row&#039;s `on_hand`: −3 writes off three, +3 finds three. A delta, not the new balance. Zero is refused (400). A correction that would take `on_hand` below zero is a 422 the database insists on; one that would take it below this row&#039;s own `reserved` is a 422 the `allow_negative_stock` setting can permit.
    reason : Optional[str]
        Why this row is being corrected, written onto the ledger booking. Owed unless `movement_reason_required` is &#039;none&#039;.
    """
    quantity: float = Field(..., alias='quantity')
    reason: Optional[str] = Field(default=None, alias='reason')
