from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderCompleteRequest(AppwriteModel):
    """
    No required fields — send {}.

    Attributes
    ----------
    completed_by : Optional[str]
        Who closed the order, as the caller reports it. Not stored on the order: it is carried in the order.completed event&#039;s payload, which is where the audit trail keeps who did what. Free text, not resolved against a user directory.
    """
    completed_by: Optional[str] = Field(default=None, alias='completed_by')
