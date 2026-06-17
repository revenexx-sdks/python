from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class InventoryReleaseRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    order_ref : str
        The order whose active reservations are released.
    """
    order_ref: str = Field(..., alias='order_ref')
