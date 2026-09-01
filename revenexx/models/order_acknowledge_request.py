from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderAcknowledgeRequest(AppwriteModel):
    """
    The acknowledgement carries one field, and it is optional: sending {} still stamps acknowledged_at, which is the point of the call. acknowledged_at is the server&#039;s clock and is never taken from the body.

    Attributes
    ----------
    external_ref : Optional[str]
        The FULFILLING system&#039;s reference for this order, typically the ERP order number. Written once by POST /orders/{id}/acknowledge and null until an integration acknowledged it. Keeps the existing value when omitted.
    """
    external_ref: Optional[str] = Field(default=None, alias='external_ref')
