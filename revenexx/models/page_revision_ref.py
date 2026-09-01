from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PageRevisionRef(AppwriteModel):
    """
    One publication of this page, without the snapshot — who published, when, and under what name.

    Attributes
    ----------
    created_at : Optional[str]
        When this revision was published.
    created_by : Optional[str]
        The user id that published.
    created_by_name : Optional[str]
        That user&#039;s display name, copied in at publish time so the history stays readable after the user is gone.
    id : Optional[str]
        The revision id. A page&#039;s `published_revision_id` points at one of these, and it is the only thing delivery reads.
    label : Optional[str]
        What this publication was called, e.g. &quot;Autumn campaign&quot;. It is what turns the history into a list of changes rather than a list of timestamps.
    page_id : Optional[str]
        The page this revision belongs to.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    created_by: Optional[str] = Field(default=None, alias='created_by')
    created_by_name: Optional[str] = Field(default=None, alias='created_by_name')
    id: Optional[str] = Field(default=None, alias='id')
    label: Optional[str] = Field(default=None, alias='label')
    page_id: Optional[str] = Field(default=None, alias='page_id')
