from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.price_list_status import PriceListStatus
from ..enums.price_list_tax_basis import PriceListTaxBasis

class PriceListUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    channel_id : Optional[str]
        Scope: only this sales channel. Beats the open lists, loses to contact and organization.
    code : Optional[str]
        Unique list code per tenant — the handle every import and integration addresses this list by. A code already in use answers 409.
    contact_id : Optional[str]
        Scope: only this contact. The most specific scope there is — it beats organization, channel and every open list, whatever their priority.
    currency : Optional[str]
        ISO 4217 code (default EUR) — the currency of EVERY amount in this list, since entries carry none of their own. Resolution only considers lists matching the currency of the call; nothing is ever converted.
    description : Optional[str]
        Free text for whoever maintains the list — why it exists and who it is for. Never shown to a buyer.
    is_default : Optional[bool]
        The fallback list. Within its group it sorts LAST, so it wins only where nothing more specific priced the item. Use prices.lists.make-default to move the flag rather than setting it here — two defaults leave a tie to row order.
    labels : Optional[Dict[str, Any]]
        Localised names, keyed by language tag — {&quot;de&quot;: &quot;Händlerpreise&quot;, &quot;en&quot;: &quot;Dealer prices&quot;}. Omit to show `name` everywhere.
    metadata : Optional[Dict[str, Any]]
        Free-form bag: whatever JSON object you write round-trips exactly, and this app never reads it. Its keys are yours — ERP provenance is the usual content.
    name : Optional[str]
        Operator-facing name, shown wherever a human picks a list.
    organization_id : Optional[str]
        Scope: only buyers of this organization. Beats channel-scoped and open lists.
    priority : Optional[float]
        Tie-break WITHIN a specificity group (higher wins, default 0). It never beats scope: an organization list at 0 still wins over an open list at 100.
    requires_auth : Optional[bool]
        Gate: when true the list resolves only for an authenticated buyer (contact or organization context); anonymous resolve calls get on_request. Default false (open to everyone).
    status : Optional[PriceListStatus]
        Default &#039;active&#039; — only active lists resolve. &#039;inactive&#039; retires a list without deleting its prices.
    tax_basis : Optional[PriceListTaxBasis]
        Whether the amounts in this list are net (tax excluded) or gross (tax included) — the one fact a price cannot be without. Omit (null) to inherit the tenant&#039;s tax_inclusive_default setting; the resolve answer names which of the two decided under tax_basis_source.
    tax_included : Optional[bool]
        LEGACY mirror of tax_basis. false is the column default and is NOT read as a statement of intent; true is read as gross, and only where tax_basis is null. Prefer tax_basis.
    valid_from : Optional[str]
        Start of the validity window of the WHOLE list (ISO 8601); null = open-ended. Outside it the list is not a candidate at all.
    valid_until : Optional[str]
        End of the validity window of the whole list; null = open-ended. Lets a season expire on its own instead of being deactivated by hand.
    """
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    code: Optional[str] = Field(default=None, alias='code')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    currency: Optional[str] = Field(default=None, alias='currency')
    description: Optional[str] = Field(default=None, alias='description')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    name: Optional[str] = Field(default=None, alias='name')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
    priority: Optional[float] = Field(default=None, alias='priority')
    requires_auth: Optional[bool] = Field(default=None, alias='requires_auth')
    status: Optional[PriceListStatus] = Field(default=None, alias='status')
    tax_basis: Optional[PriceListTaxBasis] = Field(default=None, alias='tax_basis')
    tax_included: Optional[bool] = Field(default=None, alias='tax_included')
    valid_from: Optional[str] = Field(default=None, alias='valid_from')
    valid_until: Optional[str] = Field(default=None, alias='valid_until')
