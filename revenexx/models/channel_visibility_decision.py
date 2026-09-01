from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.channel_visibility_reason import ChannelVisibilityReason

class ChannelVisibilityDecision(AppwriteModel):
    """
    

    Attributes
    ----------
    id : Optional[str]
        The id as it was sent, verbatim.
    reason : Optional[ChannelVisibilityReason]
        Why the row was shown or hidden — the answer is auditable, not a bare boolean.
    visible : Optional[bool]
        Whether this row may be shown in the resolved channel. The same answer as membership in `visible`; `reason` says why.
    """
    id: Optional[str] = Field(default=None, alias='id')
    reason: Optional[ChannelVisibilityReason] = Field(default=None, alias='reason')
    visible: Optional[bool] = Field(default=None, alias='visible')
