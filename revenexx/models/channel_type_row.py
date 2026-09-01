from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.channel_type_tone import ChannelTypeTone

class ChannelTypeRow(AppwriteModel):
    """
    

    Attributes
    ----------
    code : Optional[str]
        What `channels.type` stores. Immutable once created — renaming it would orphan every channel that carries it, and there is no FK behind `channels.type` to cascade. A fresh install seeds storefront, punchout, marketplace, api, pos; a merchant may retire any of them and add their own.
    created_at : Optional[str]
        When the row was inserted, set by the database.
    description : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    descriptions : Optional[Dict[str, Any]]
        A locale map keyed by language tag: {&quot;en&quot;: …, &quot;de&quot;: …}. Read the requested tag and fall back to the plain column beside it.
    id : Optional[str]
        Row id, and the only handle GET/PUT/DELETE /channels/types/{id} accept. Not the type `code`. No example is published because no id this app could invent names a row a tenant holds.
    is_default : Optional[bool]
        The type a channel created without one gets. Exactly one row carries it.
    is_system : Optional[bool]
        Seeded on install rather than added by the merchant. A flag about origin only — a system type is still renameable, reorderable and retirable.
    labels : Optional[Dict[str, Any]]
        A locale map keyed by language tag: {&quot;en&quot;: …, &quot;de&quot;: …}. Read the requested tag and fall back to the plain column beside it.
    position : Optional[float]
        Sort position. GET /channels/types always answers in this order and takes no `order` parameter. It is not unique and defaults to 0, so ties are broken by `code` — the order is total, which is what makes paging the list safe to walk.
    tenant_id : Optional[str]
        The tenant that owns this row. Added by the data plane, not by this app: it is not a column of schema.json, so it is read-only and `?tenant_id=` is not a filter — the key is silently dropped and never reaches the `filter` echo.
    title : Optional[Dict[str, Any]]
        The fallback name. `labels` carries the per-locale ones. Rows seeded before 0.7.0 hold a serialized locale map here instead (PE-452).
    tone : Optional[ChannelTypeTone]
        Semantic badge colour for this type, for a client that renders the list. The client owns what each tone looks like; the value only says what it MEANS.
    updated_at : Optional[str]
        When the row was last written, set by the database.
    """
    code: Optional[str] = Field(default=None, alias='code')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    descriptions: Optional[Dict[str, Any]] = Field(default=None, alias='descriptions')
    id: Optional[str] = Field(default=None, alias='id')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    is_system: Optional[bool] = Field(default=None, alias='is_system')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    position: Optional[float] = Field(default=None, alias='position')
    tenant_id: Optional[str] = Field(default=None, alias='tenant_id')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
    tone: Optional[ChannelTypeTone] = Field(default=None, alias='tone')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
