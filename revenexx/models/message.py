from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Message(AppwriteModel):
    """
    

    Attributes
    ----------
    attachments : Optional[List[Any]]
        Typed model field.
    attempts : float
        Typed model field.
    binding_id : Optional[str]
        Typed model field.
    channel : str
        Typed model field.
    click_count : float
        Typed model field.
    clicked_at : Optional[str]
        Typed model field.
    created_at : str
        Typed model field.
    data : Optional[List[Any]]
        Typed model field.
    delivered_at : Optional[str]
        Typed model field.
    error : Optional[str]
        Typed model field.
    from_draft : bool
        Typed model field.
    id : str
        Typed model field.
    idempotency_fingerprint : Optional[str]
        Typed model field.
    idempotency_key : Optional[str]
        Typed model field.
    locale : Optional[str]
        Typed model field.
    market : Optional[str]
        Typed model field.
    message_class : str
        Typed model field.
    open_count : float
        Typed model field.
    opened_at : Optional[str]
        Typed model field.
    provider_message_id : Optional[str]
        Typed model field.
    scheduled_for : Optional[str]
        Typed model field.
    sent_at : Optional[str]
        Typed model field.
    source_event_id : Optional[str]
        Typed model field.
    status : str
        Typed model field.
    subject : Optional[str]
        Typed model field.
    suppression_reason : Optional[str]
        Typed model field.
    template_key : Optional[str]
        Typed model field.
    tenant_id : str
        Typed model field.
    to : str
        Typed model field.
    """
    attachments: Optional[List[Any]] = Field(..., alias='attachments')
    attempts: float = Field(..., alias='attempts')
    binding_id: Optional[str] = Field(..., alias='binding_id')
    channel: str = Field(..., alias='channel')
    click_count: float = Field(..., alias='click_count')
    clicked_at: Optional[str] = Field(..., alias='clicked_at')
    created_at: str = Field(..., alias='created_at')
    data: Optional[List[Any]] = Field(..., alias='data')
    delivered_at: Optional[str] = Field(..., alias='delivered_at')
    error: Optional[str] = Field(..., alias='error')
    from_draft: bool = Field(..., alias='from_draft')
    id: str = Field(..., alias='id')
    idempotency_fingerprint: Optional[str] = Field(..., alias='idempotency_fingerprint')
    idempotency_key: Optional[str] = Field(..., alias='idempotency_key')
    locale: Optional[str] = Field(..., alias='locale')
    market: Optional[str] = Field(..., alias='market')
    message_class: str = Field(..., alias='message_class')
    open_count: float = Field(..., alias='open_count')
    opened_at: Optional[str] = Field(..., alias='opened_at')
    provider_message_id: Optional[str] = Field(..., alias='provider_message_id')
    scheduled_for: Optional[str] = Field(..., alias='scheduled_for')
    sent_at: Optional[str] = Field(..., alias='sent_at')
    source_event_id: Optional[str] = Field(..., alias='source_event_id')
    status: str = Field(..., alias='status')
    subject: Optional[str] = Field(..., alias='subject')
    suppression_reason: Optional[str] = Field(..., alias='suppression_reason')
    template_key: Optional[str] = Field(..., alias='template_key')
    tenant_id: str = Field(..., alias='tenant_id')
    to: str = Field(..., alias='to')
