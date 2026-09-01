from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_return_settlement import OrderReturnSettlement

class OrderReturnCompleteRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    resolution : Optional[OrderReturnSettlement]
        How the return was settled. Omitted = settled without recording how.
    """
    resolution: Optional[OrderReturnSettlement] = Field(default=None, alias='resolution')
