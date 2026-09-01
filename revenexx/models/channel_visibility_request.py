from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .channel_visibility_item import ChannelVisibilityItem

class ChannelVisibilityRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    channel : Optional[str]
        The channel `code` (the scope slug) to evaluate against, trimmed and lowercased before it is matched. Optional, and through api.revenexx.com it is the ONLY way to name a channel explicitly: the x-revenexx-channel header is not forwarded to the app, so without this the resolution falls through to the scope_context.channel claim and then to the tenant&#039;s default channel. A code no channel carries is not an error — the answer is resolved:false with reason &#039;unknown_channel&#039;, so a caller can tell it from an outage.
    items : List[ChannelVisibilityItem]
        The rows to decide on, each with the channel assignments Baseline holds for it. POST /api/v1/scopes/lookup?dimension=channel answers in exactly this shape. At most 500 — Baseline&#039;s own lookup ceiling.
    """
    channel: Optional[str] = Field(default=None, alias='channel')
    items: List[ChannelVisibilityItem] = Field(..., alias='items')
