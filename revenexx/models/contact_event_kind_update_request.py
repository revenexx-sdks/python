from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.contact_event_kind_update_request_tone import ContactEventKindUpdateRequestTone

class ContactEventKindUpdateRequest(AppwriteModel):
    """
    Everything but `code`. Sending a different one is a 400 rather than a silent no-op, because records already store it.

    Attributes
    ----------
    description : Optional[str]
        One line of help for whoever picks this value.
    descriptions : Optional[Dict[str, Any]]
        Localized descriptions, keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Null when nobody translated this value — a client then falls back to `description`.
    is_default : Optional[bool]
        Promote this value; the previous default is demoted.
    labels : Optional[Dict[str, Any]]
        Localized titles, keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Null when nobody translated this value — a client then falls back to `title`.
    position : Optional[float]
        Where it sits in the set, ascending.
    title : Optional[str]
        The fallback name shown when no locale matches.
    tone : Optional[ContactEventKindUpdateRequestTone]
        Semantic badge colour.
    """
    description: Optional[str] = Field(default=None, alias='description')
    descriptions: Optional[Dict[str, Any]] = Field(default=None, alias='descriptions')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
    title: Optional[str] = Field(default=None, alias='title')
    tone: Optional[ContactEventKindUpdateRequestTone] = Field(default=None, alias='tone')
