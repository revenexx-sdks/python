from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.price_list_status import PriceListStatus

class PriceListCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    channel_id : Optional[str]
        Scope: only this channel.
    code : str
        Unique list code per tenant.
    contact_id : Optional[str]
        Scope: only this contact — beats every other scope.
    currency : Optional[str]
        ISO 4217 code (default EUR) — resolution only considers lists matching the requested currency.
    description : Optional[str]
        Typed model field.
    is_default : Optional[bool]
        Default lists resolve last within their group.
    labels : Optional[Dict[str, Any]]
        Localised names ({de, en, …}).
    market_id : Optional[str]
        Scope: only this market.
    metadata : Optional[Dict[str, Any]]
        Free-form metadata.
    name : str
        Typed model field.
    organization_id : Optional[str]
        Scope: only this organization.
    priority : Optional[float]
        Tie-breaker within a specificity group (higher wins, default 0).
    status : Optional[PriceListStatus]
        Default &#039;active&#039; — only active lists resolve.
    tax_included : Optional[bool]
        Gross (true) or net (false, default) prices.
    valid_from : Optional[str]
        Validity window start.
    valid_until : Optional[str]
        Validity window end.
    """
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    code: str = Field(..., alias='code')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    currency: Optional[str] = Field(default=None, alias='currency')
    description: Optional[str] = Field(default=None, alias='description')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    market_id: Optional[str] = Field(default=None, alias='market_id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: str = Field(..., alias='name')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    priority: Optional[float] = Field(default=None, alias='priority')
    status: Optional[PriceListStatus] = Field(default=None, alias='status')
    tax_included: Optional[bool] = Field(default=None, alias='tax_included')
    valid_from: Optional[str] = Field(default=None, alias='valid_from')
    valid_until: Optional[str] = Field(default=None, alias='valid_until')
