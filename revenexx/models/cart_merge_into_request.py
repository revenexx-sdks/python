from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CartMergeIntoRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    target_cart_id : str
        Receiving cart (must be active). The cart in the path is the source and becomes status merged.
    """
    target_cart_id: str = Field(..., alias='target_cart_id')
