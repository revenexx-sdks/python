from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CartClaimRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    contact_id : str
        Contact taking ownership.
    session_key : str
        Guest session whose active carts are handed over.
    target_cart_id : Optional[str]
        Merge the session carts into this cart instead of adopting them.
    """
    contact_id: str = Field(..., alias='contact_id')
    session_key: str = Field(..., alias='session_key')
    target_cart_id: Optional[str] = Field(default=None, alias='target_cart_id')
