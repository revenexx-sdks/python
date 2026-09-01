from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.contact_activity_kind import ContactActivityKind

class ContactActivityRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    actor : Optional[str]
        Who logged it (operator id or email). Free text; this app does not resolve it.
    kind : Optional[ContactActivityKind]
        What happened. &#039;system&#039; is deliberately NOT accepted — those rows are the registration decision trail and are written by the approve/reject routes. Default &#039;note&#039;.
    note : Optional[str]
        The long form. Stored inside the event payload as `note`, not as a column of its own.
    occurred_at : Optional[str]
        When it actually happened. Defaults to now — a call logged on Monday about Friday should say Friday.
    subject : str
        One line a person can scan in a timeline. Required — an entry nobody can read at a glance is not worth the row.
    """
    actor: Optional[str] = Field(default=None, alias='actor')
    kind: Optional[ContactActivityKind] = Field(default=None, alias='kind')
    note: Optional[str] = Field(default=None, alias='note')
    occurred_at: Optional[str] = Field(default=None, alias='occurred_at')
    subject: str = Field(..., alias='subject')
