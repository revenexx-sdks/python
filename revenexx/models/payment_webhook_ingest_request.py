from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PaymentWebhookIngestRequest(AppwriteModel):
    """
    The dispatch envelope from webhooks.revenexx.com. Nothing is required and nothing is constrained — three keys are read, and the rest is carried along.

    Attributes
    ----------
    id : Optional[str]
        The dispatcher&#039;s delivery id. Echoed back as `delivery_id` so a delivery and what the ledger did can be correlated.
    request : Optional[str]
        The captured HTTP request as the PSP sent it.
    verified : Optional[str]
        Whether the ingress verified the callback signature against the provider&#039;s `webhook_secret`. An explicit false is refused with 422: an endpoint may run in annotate mode, and the ledger stays sovereign over one that does.
    """
    id: Optional[str] = Field(default=None, alias='id')
    request: Optional[str] = Field(default=None, alias='request')
    verified: Optional[str] = Field(default=None, alias='verified')
