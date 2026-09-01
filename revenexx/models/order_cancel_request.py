from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderCancelRequest(AppwriteModel):
    """
    Cancels the WHOLE order, and only while nothing has shipped. Both fields are optional unless the tenant requires a reason.

    Attributes
    ----------
    cancelled_by : Optional[str]
        Who cancelled, as the caller reported it — an operator, a desk, a system. Free text; this app does not resolve it against a user directory.
    reason : Optional[str]
        Why it was cancelled, free text. Mandatory when the tenant sets cancel_requires_reason — for those merchants an unexplained cancellation is refused with a 400.
    """
    cancelled_by: Optional[str] = Field(default=None, alias='cancelled_by')
    reason: Optional[str] = Field(default=None, alias='reason')
