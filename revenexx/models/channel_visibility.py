from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .channel_visibility_counts import ChannelVisibilityCounts
from .channel_visibility_decision import ChannelVisibilityDecision
from .channel_policy import ChannelPolicy
from ..enums.channel_unresolved_reason import ChannelUnresolvedReason
from ..enums.channel_context_source import ChannelContextSource

class ChannelVisibility(AppwriteModel):
    """
    

    Attributes
    ----------
    channel : Optional[str]
        The channel that resolved, or null. Null on every answer where `resolved` is false — including the everyday one on a tenant that has not created a channel yet.
    counts : Optional[ChannelVisibilityCounts]
        The three tallies, so a caller can log or alert on a batch without walking it.
    default_ambiguous : Optional[bool]
        More than one channel claims is_default; the lowest position wins and this says so.
    hidden : Optional[List[Any]]
        Just the ids that must NOT be shown. The complement of `visible`; together they are every id sent, so a caller can assert nothing was dropped.
    items : Optional[List[ChannelVisibilityDecision]]
        One decision per row sent, in the order they were sent, so a caller can zip it back onto its own list without matching on id.
    policy : Optional[ChannelPolicy]
        The visibility policy in force for the resolved channel.
    reason : Optional[ChannelUnresolvedReason]
        Why not, when resolved is false. Null when it resolved.
    requested : Optional[str]
        The channel code the request named, if any — lowercased and trimmed as it was matched.
    resolved : Optional[bool]
        Whether a channel could be resolved for this request.
    source : Optional[ChannelContextSource]
        Where the channel came from, in the order they are tried: &#039;body&#039; (the `channel` field, POST /channels/visibility only), &#039;query&#039; (`?channel=`), &#039;header&#039; (x-revenexx-channel), &#039;jwt&#039; (the scope_context.channel claim), then &#039;default&#039; (the channel flagged is_default). Null when nothing resolved. Note that &#039;header&#039; is not reachable through api.revenexx.com: the gateway builds a fresh request to the app and copies a fixed set of headers into it, and x-revenexx-channel is not among them — see `policy.header`.
    visible : Optional[List[Any]]
        Just the ids that may be shown, ready to filter a result set with — the same rows `items` marks visible:true, without the reasons.
    """
    channel: Optional[str] = Field(default=None, alias='channel')
    counts: Optional[ChannelVisibilityCounts] = Field(default=None, alias='counts')
    default_ambiguous: Optional[bool] = Field(default=None, alias='default_ambiguous')
    hidden: Optional[List[Any]] = Field(default=None, alias='hidden')
    items: Optional[List[ChannelVisibilityDecision]] = Field(default=None, alias='items')
    policy: Optional[ChannelPolicy] = Field(default=None, alias='policy')
    reason: Optional[ChannelUnresolvedReason] = Field(default=None, alias='reason')
    requested: Optional[str] = Field(default=None, alias='requested')
    resolved: Optional[bool] = Field(default=None, alias='resolved')
    source: Optional[ChannelContextSource] = Field(default=None, alias='source')
    visible: Optional[List[Any]] = Field(default=None, alias='visible')
