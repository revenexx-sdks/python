from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.channel_inactive_behavior import ChannelInactiveBehavior
from ..enums.channel_policy_source import ChannelPolicySource
from ..enums.channel_policy_tenant_default import ChannelPolicyTenantDefault
from ..enums.channel_unassigned_policy import ChannelUnassignedPolicy

class ChannelPolicy(AppwriteModel):
    """
    The visibility policy in force for the resolved channel.

    Attributes
    ----------
    dimension : Optional[str]
        Always &#039;channel&#039; — the scope dimension this app provides.
    header : Optional[str]
        The header name Baseline uses for this dimension. Through api.revenexx.com it does NOT reach the app — the gateway builds a fresh request downstream and forwards only its own headers — so use `?channel=` (or `channel` in the body of POST /channels/visibility) instead. The header path applies to a direct in-cluster call to the app.
    inactive_channel_behavior : Optional[ChannelInactiveBehavior]
        The tenant setting, echoed: what `status = &#039;inactive&#039;` DOES. &#039;serve&#039; makes it a label and the channel still resolves; &#039;block&#039; makes resolution fail with reason &#039;channel_inactive&#039;, and the policy then falls back to the tenant answer.
    jwt_path : Optional[str]
        The claim path in the forwarded identity token that names the active channel, tried after the query and the header and before the default channel.
    match_mode : Optional[str]
        How Baseline matches the dimension — &#039;single&#039;: a request is in exactly one channel at a time, never a set.
    require_channel_context : Optional[bool]
        The tenant setting, echoed: whether a request naming no channel is refused rather than falling back to the default channel. On POST /channels/visibility that refusal is the single 400 this app makes of its own accord.
    source : Optional[ChannelPolicySource]
        Whether the answer came from the tenant setting or this channel&#039;s own override. Only a channel that actually resolved gets a say — a blocked or unknown channel falls back to &#039;tenant&#039;.
    tenant_default : Optional[ChannelPolicyTenantDefault]
        The tenant-wide baseline, so a caller can see what this channel overrode. Equal to `unassigned_visibility` whenever `source` is &#039;tenant&#039;.
    unassigned_visibility : Optional[ChannelUnassignedPolicy]
        What a row with NO channel assignment means. &#039;all&#039; is Baseline&#039;s open-by-default semantic, reproduced exactly; &#039;assigned_only&#039; is the closed assortment the _scoped view cannot express.
    """
    dimension: Optional[str] = Field(default=None, alias='dimension')
    header: Optional[str] = Field(default=None, alias='header')
    inactive_channel_behavior: Optional[ChannelInactiveBehavior] = Field(default=None, alias='inactive_channel_behavior')
    jwt_path: Optional[str] = Field(default=None, alias='jwt_path')
    match_mode: Optional[str] = Field(default=None, alias='match_mode')
    require_channel_context: Optional[bool] = Field(default=None, alias='require_channel_context')
    source: Optional[ChannelPolicySource] = Field(default=None, alias='source')
    tenant_default: Optional[ChannelPolicyTenantDefault] = Field(default=None, alias='tenant_default')
    unassigned_visibility: Optional[ChannelUnassignedPolicy] = Field(default=None, alias='unassigned_visibility')
