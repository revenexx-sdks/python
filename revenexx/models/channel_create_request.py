from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.channel_status import ChannelStatus
from ..enums.channel_unassigned_visibility import ChannelUnassignedVisibility

class ChannelCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        Stable channel code, unique per tenant (e.g. shop, punchout-acme). It is the scope slug Baseline matches channel assignments on, so it is held to Baseline&#039;s own shape: lowercase a-z/0-9 first, then a-z/0-9/_/-, up to 63 characters. Anything else is refused — a code that cannot be a scope slug leaves the channel unable to filter.
    is_default : Optional[bool]
        Mark as the default channel (default false). At most one channel carries it — setting it demotes the previous holder.
    labels : Optional[Dict[str, Any]]
        Localized display names. A locale map keyed by language tag: {&quot;en&quot;: …, &quot;de&quot;: …}. Read the requested tag and fall back to the plain column beside it.
    name : str
        Display name.
    position : Optional[float]
        Sort position (default 0).
    status : Optional[ChannelStatus]
        Lifecycle status (default &#039;active&#039;). Whether the channel is in service. What &#039;inactive&#039; DOES is the tenant&#039;s inactive_channel_behavior setting: on &#039;serve&#039; it is a label and the channel still resolves, on &#039;block&#039; /channels/context answers resolved:false with reason &#039;channel_inactive&#039;. Served as the &#039;channels.statuses&#039; vocabulary.
    type : Optional[str]
        Which channel type this is. One of the codes the tenant keeps under GET /channels/types — served with labels as the &#039;channels.types&#039; vocabulary. Deliberately NOT an enum: the set is the tenant&#039;s own rows, not a CHECK constraint this repo could quote. A fresh install starts with storefront, punchout, marketplace, api, pos, which is why &#039;storefront&#039; is the example here, but a merchant may rename or retire any of them and add their own (a feed or a print channel), so read the list rather than assuming it. Omitted on create it falls back to the type the tenant flagged as their default, never to a hardcoded value; a code the tenant does not keep is a 400 that names the ones they do.
    unassigned_visibility : Optional[ChannelUnassignedVisibility]
        Default &#039;inherit&#039;. What it means, IN THIS CHANNEL, that a row carries no channel assignment at all — the per-channel override of the tenant-wide unassigned_channel_visibility setting. &#039;inherit&#039; (the default) takes the tenant&#039;s answer and changes nothing. &#039;all&#039; shows unassigned rows: everything is on sale unless somebody carved it out, which is what an open storefront wants and what Baseline&#039;s is_visible() does today. &#039;assigned_only&#039; hides them until they are explicitly assigned — the negotiated assortment a punchout contract describes, and the one answer the generated _scoped view has no way to express, which is why POST /channels/visibility exists to apply it. Rows that DO carry assignments are unaffected either way. Served with its labels as the &#039;channels.unassigned-visibility&#039; vocabulary.
    """
    code: str = Field(..., alias='code')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    name: str = Field(..., alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    status: Optional[ChannelStatus] = Field(default=None, alias='status')
    type: Optional[str] = Field(default=None, alias='type')
    unassigned_visibility: Optional[ChannelUnassignedVisibility] = Field(default=None, alias='unassigned_visibility')
