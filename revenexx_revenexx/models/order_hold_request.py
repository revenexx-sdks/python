from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderHoldRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    reason : Optional[str]
        Why the order is blocked (shown on the shipping guard).
    """
    reason: Optional[str] = Field(default=None, alias='reason')
