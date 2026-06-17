from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .order_return_position import OrderReturnPosition

class OrderReturnCreateRequest(AppwriteModel):
    """
    Register a return against the shipped quantities — the return number is drawn from the &#039;return&#039; range.

    Attributes
    ----------
    metadata : Optional[Dict[str, Any]]
        Free-form metadata.
    positions : List[OrderReturnPosition]
        Typed model field.
    reason : Optional[str]
        Typed model field.
    """
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    positions: List[OrderReturnPosition] = Field(..., alias='positions')
    reason: Optional[str] = Field(default=None, alias='reason')
