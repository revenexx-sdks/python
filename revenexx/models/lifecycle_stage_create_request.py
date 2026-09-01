from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.lifecycle_stage_create_request_tone import LifecycleStageCreateRequestTone

class LifecycleStageCreateRequest(AppwriteModel):
    """
    Add one value to the lifecycle stages set. It is available to `organizations.lifecycle_stage` immediately.

    Attributes
    ----------
    code : str
        What `organizations.lifecycle_stage` will store. Lowercase, starting with a letter; immutable afterwards.
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
    tone : Optional[LifecycleStageCreateRequestTone]
        Semantic badge colour.
    """
    code: str = Field(..., alias='code')
    description: Optional[str] = Field(default=None, alias='description')
    descriptions: Optional[Dict[str, Any]] = Field(default=None, alias='descriptions')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
    title: str = Field(..., alias='title')
    tone: Optional[LifecycleStageCreateRequestTone] = Field(default=None, alias='tone')
