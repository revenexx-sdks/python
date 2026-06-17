from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderCancelRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    cancelled_by : Optional[str]
        Acting user/system.
    reason : Optional[str]
        Typed model field.
    """
    cancelled_by: Optional[str] = Field(default=None, alias='cancelled_by')
    reason: Optional[str] = Field(default=None, alias='reason')
