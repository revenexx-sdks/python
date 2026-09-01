from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.contact_event_kind_create_request_tone import ContactEventKindCreateRequestTone

class ContactEventKindCreateRequest(AppwriteModel):
    """
    Add one value to the activity types set. It is available to `contact_events.kind` immediately.

    Attributes
    ----------
    code : str
        What `contact_events.kind` will store. Lowercase, starting with a letter; immutable afterwards.
    description : Optional[str]
        One line of help for whoever picks this value.
    descriptions : Optional[Dict[str, Any]]
        Localized descriptions, keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Null when nobody translated this value — a client then falls back to `description`.
    is_default : Optional[bool]
        Promote this value; the previous default is demoted in the same call.
    labels : Optional[Dict[str, Any]]
        Localized titles, keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Null when nobody translated this value — a client then falls back to `title`.
    position : Optional[float]
        Where it sits in the set, ascending. Default 0.
    title : str
        The fallback name shown when no locale matches.
    tone : Optional[ContactEventKindCreateRequestTone]
        Semantic badge colour.
    """
    code: str = Field(..., alias='code')
    description: Optional[str] = Field(default=None, alias='description')
    descriptions: Optional[Dict[str, Any]] = Field(default=None, alias='descriptions')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
    title: str = Field(..., alias='title')
    tone: Optional[ContactEventKindCreateRequestTone] = Field(default=None, alias='tone')
