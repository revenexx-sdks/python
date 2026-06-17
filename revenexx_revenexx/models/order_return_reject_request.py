from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderReturnRejectRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    reason : Optional[str]
        Fallback for &#039;resolution&#039;.
    resolution : Optional[str]
        Why the return was rejected.
    """
    reason: Optional[str] = Field(default=None, alias='reason')
    resolution: Optional[str] = Field(default=None, alias='resolution')
