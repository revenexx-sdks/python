from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.channel_status import ChannelStatus
from ..enums.channel_unassigned_visibility import ChannelUnassignedVisibility

class Channel(AppwriteModel):
    """
    

    Attributes
    ----------
    code : Optional[str]
        The scope slug Baseline matches channel assignments on (manifest.provides_scopes[].slug_source). Unique per tenant and, in practice, immutable — changing it orphans every assignment made against it.
    created_at : Optional[str]
        When the row was inserted, set by the database.
    id : Optional[str]
        Row id, and the only handle GET/PUT/DELETE /channels/{id} accept. Not the scope slug — that is `code`. No example is published because no id this app could invent names a row a tenant holds.
    is_default : Optional[bool]
        The channel a request that names none falls back to. At most one channel carries it.
    labels : Optional[Dict[str, Any]]
        A locale map keyed by language tag: {&quot;en&quot;: …, &quot;de&quot;: …}. Read the requested tag and fall back to the plain column beside it.
    name : Optional[str]
        Display name. `labels` carries the per-locale ones.
    position : Optional[float]
        Sort position — ascending, and the tiebreak when two channels both claim is_default.
    status : Optional[ChannelStatus]
        Whether the channel is in service. What &#039;inactive&#039; DOES is the tenant&#039;s inactive_channel_behavior setting: on &#039;serve&#039; it is a label and the channel still resolves, on &#039;block&#039; /channels/context answers resolved:false with reason &#039;channel_inactive&#039;. Served as the &#039;channels.statuses&#039; vocabulary.
    tenant_id : Optional[str]
        The tenant that owns this row. Added by the data plane, not by this app: it is not a column of schema.json, so it is read-only and `?tenant_id=` is not a filter — the key is silently dropped and never reaches the `filter` echo.
    type : Optional[str]
        One of the codes the tenant keeps under GET /channels/types — served with labels as the &#039;channels.types&#039; vocabulary. Deliberately NOT an enum: the set is the tenant&#039;s own rows, not a CHECK constraint this repo could quote. A fresh install starts with storefront, punchout, marketplace, api, pos, which is why &#039;storefront&#039; is the example here, but a merchant may rename or retire any of them and add their own (a feed or a print channel), so read the list rather than assuming it.
    unassigned_visibility : Optional[ChannelUnassignedVisibility]
        What it means, IN THIS CHANNEL, that a row carries no channel assignment at all — the per-channel override of the tenant-wide unassigned_channel_visibility setting. &#039;inherit&#039; (the default) takes the tenant&#039;s answer and changes nothing. &#039;all&#039; shows unassigned rows: everything is on sale unless somebody carved it out, which is what an open storefront wants and what Baseline&#039;s is_visible() does today. &#039;assigned_only&#039; hides them until they are explicitly assigned — the negotiated assortment a punchout contract describes, and the one answer the generated _scoped view has no way to express, which is why POST /channels/visibility exists to apply it. Rows that DO carry assignments are unaffected either way. Served with its labels as the &#039;channels.unassigned-visibility&#039; vocabulary.
    updated_at : Optional[str]
        When the row was last written, set by the database.
    """
    code: Optional[str] = Field(default=None, alias='code')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    status: Optional[ChannelStatus] = Field(default=None, alias='status')
    tenant_id: Optional[str] = Field(default=None, alias='tenant_id')
    type: Optional[str] = Field(default=None, alias='type')
    unassigned_visibility: Optional[ChannelUnassignedVisibility] = Field(default=None, alias='unassigned_visibility')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
