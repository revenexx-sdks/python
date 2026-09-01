from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.shipping_service_level_update_request_tone import ShippingServiceLevelUpdateRequestTone

class ShippingServiceLevelUpdateRequest(AppwriteModel):
    """
    Everything but the code. Sending a different code is a 400 rather than a silent no-op: renaming it would orphan every row that carries it.

    Attributes
    ----------
    description : Optional[str]
        The sentence under the title, explaining when to pick this service level. Null when the title says enough.
    descriptions : Optional[Dict[str, Any]]
        Localized descriptions. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
    is_default : Optional[bool]
        Promote this value; the previous default is demoted. POST …/make-default does the same thing without an edit.
    labels : Optional[Dict[str, Any]]
        Localized titles. A flat map keyed by locale — the Cockpit falls back to `en`. Null means the row has no translations and every client shows the untranslated column instead.
    position : Optional[float]
        Sort order in a select — the collection is returned in it.
    title : Optional[str]
        What an operator reads in a select. The name a merchant renames; the code underneath never moves.
    tone : Optional[ShippingServiceLevelUpdateRequestTone]
        Semantic badge colour for a UI listing the set. The client owns what each tone looks like.
    """
    description: Optional[str] = Field(default=None, alias='description')
    descriptions: Optional[Dict[str, Any]] = Field(default=None, alias='descriptions')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
    title: Optional[str] = Field(default=None, alias='title')
    tone: Optional[ShippingServiceLevelUpdateRequestTone] = Field(default=None, alias='tone')
