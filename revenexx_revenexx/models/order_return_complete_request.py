from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderReturnCompleteRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    resolution : Optional[str]
        How the return was settled (refund, replacement, …).
    """
    resolution: Optional[str] = Field(default=None, alias='resolution')
