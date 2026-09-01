from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PushSubscription(AppwriteModel):
    """
    

    Attributes
    ----------
    created_at : Optional[str]
        Typed model field.
    endpoint : str
        Typed model field.
    id : str
        Typed model field.
    last_seen_at : Optional[str]
        Typed model field.
    subscriber_id : str
        Typed model field.
    tenant_id : str
        Typed model field.
    updated_at : Optional[str]
        Typed model field.
    user_agent : Optional[str]
        Typed model field.
    """
    created_at: Optional[str] = Field(..., alias='created_at')
    endpoint: str = Field(..., alias='endpoint')
    id: str = Field(..., alias='id')
    last_seen_at: Optional[str] = Field(..., alias='last_seen_at')
    subscriber_id: str = Field(..., alias='subscriber_id')
    tenant_id: str = Field(..., alias='tenant_id')
    updated_at: Optional[str] = Field(..., alias='updated_at')
    user_agent: Optional[str] = Field(..., alias='user_agent')
