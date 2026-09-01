from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderHoldRequest(AppwriteModel):
    """
    Stop the order. The reason is optional but is what the guard quotes back at whoever tries to ship, so an unexplained hold is a hold nobody can resolve.

    Attributes
    ----------
    reason : Optional[str]
        Why the order is held, in the words the shipping guard quotes back. Null when it is not held — releasing a hold clears it.
    """
    reason: Optional[str] = Field(default=None, alias='reason')
