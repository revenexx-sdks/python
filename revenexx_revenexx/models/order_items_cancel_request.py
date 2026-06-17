from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .order_cancel_position import OrderCancelPosition

class OrderItemsCancelRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    cancelled_by : Optional[str]
        Acting user/system.
    positions : List[OrderCancelPosition]
        Typed model field.
    reason : Optional[str]
        Typed model field.
    """
    cancelled_by: Optional[str] = Field(default=None, alias='cancelled_by')
    positions: List[OrderCancelPosition] = Field(..., alias='positions')
    reason: Optional[str] = Field(default=None, alias='reason')
