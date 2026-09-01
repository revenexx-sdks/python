from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .order_return_position import OrderReturnPosition

class OrderReturnCreateRequest(AppwriteModel):
    """
    Register a return against the shipped quantities — the return number is drawn from the return range. Omitted positions = every position that still has a returnable quantity, in full (&#039;the customer sent it all back&#039;).

    Attributes
    ----------
    metadata : Optional[Dict[str, Any]]
        Free-form data for the caller — the returns portal&#039;s own reference. Stored and returned untouched.
    positions : Optional[List[OrderReturnPosition]]
        What is coming back. Omitted = every position with a returnable (shipped, not yet returned) quantity, in full.
    reason : Optional[str]
        Why the goods are coming back, free text as the customer or the desk stated it. Also what /reject stores when it is given no resolution out of the published set.
    restock : Optional[bool]
        The default restock flag for positions that carry none of their own — and the only way to say &quot;put it all back into stock&quot; when the positions are defaulted. It does not restock anything itself: it decides what the completion REPORTS for the orchestrator&#039;s inventories.restock call.
    """
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    positions: Optional[List[OrderReturnPosition]] = Field(default=None, alias='positions')
    reason: Optional[str] = Field(default=None, alias='reason')
    restock: Optional[bool] = Field(default=None, alias='restock')
