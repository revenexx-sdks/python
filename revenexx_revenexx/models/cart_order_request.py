from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CartOrderRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    order_ref : Optional[str]
        External order reference from order management.
    """
    order_ref: Optional[str] = Field(default=None, alias='order_ref')
