from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Binding(AppwriteModel):
    """
    

    Attributes
    ----------
    channel : str
        Typed model field.
    created_at : Optional[str]
        Typed model field.
    enabled : bool
        Typed model field.
    event_topic : str
        Typed model field.
    fallback_order : float
        Typed model field.
    id : str
        Typed model field.
    locale : Optional[str]
        Typed model field.
    recipient : str
        Typed model field.
    template_key : str
        Typed model field.
    tenant_id : str
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    """
    channel: str = Field(..., alias='channel')
    created_at: Optional[str] = Field(..., alias='created_at')
    enabled: bool = Field(..., alias='enabled')
    event_topic: str = Field(..., alias='event_topic')
    fallback_order: float = Field(..., alias='fallback_order')
    id: str = Field(..., alias='id')
    locale: Optional[str] = Field(..., alias='locale')
    recipient: str = Field(..., alias='recipient')
    template_key: str = Field(..., alias='template_key')
    tenant_id: str = Field(..., alias='tenant_id')
    updated_at: Optional[str] = Field(..., alias='updated_at')
