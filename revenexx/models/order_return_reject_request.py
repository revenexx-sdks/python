from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_return_refusal import OrderReturnRefusal

class OrderReturnRejectRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    reason : Optional[str]
        Free-text fallback for &#039;resolution&#039; — a sentence about this one return, not a value out of the set.
    resolution : Optional[OrderReturnRefusal]
        Why the return was refused.
    """
    reason: Optional[str] = Field(default=None, alias='reason')
    resolution: Optional[OrderReturnRefusal] = Field(default=None, alias='resolution')
