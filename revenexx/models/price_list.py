from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.price_list_status import PriceListStatus
from ..enums.price_list_tax_basis import PriceListTaxBasis

class PriceList(AppwriteModel):
    """
    A price list: one currency, one tax basis, one validity window, one buyer scope — and the entries that price items in it. Which list wins for a given buyer is decided by scope first, then priority, then the default flag; see prices.resolve.

    Attributes
    ----------
    channel_id : Optional[str]
        Buyer scope: this list prices for this sales channel. Beats the open lists, loses to contact and organization scope.
    code : Optional[str]
        The unique per-tenant handle of the list — what an import, an ERP export and every integration addresses it by, and what the `default_price_list_code` setting names. It is never quietly reassigned: a second list under a code that is taken answers 409.
    contact_id : Optional[str]
        Buyer scope: this list prices for this one contact. The most specific scope there is — it beats organization, channel and every open list, whatever their priority.
    created_at : Optional[str]
        When the list was created. Also the `newest` tie-break’s input when the tenant settles genuine ties that way.
    currency : Optional[str]
        ISO 4217 currency of EVERY amount in this list — entries carry no currency of their own, so this is the one that governs them. Resolution only ever considers lists whose currency equals the currency of the call: a list in another currency is not converted, it simply does not price the item. This app never converts between currencies.
    description : Optional[str]
        Free text for whoever maintains the list — why it exists and who it is for. Never shown to a buyer.
    id : Optional[str]
        The price list itself. Every sub-route addresses the list by this id, and a resolve answer names the list that priced an item under `price_list.id`.
    is_default : Optional[bool]
        The fallback list. Within its group it deliberately sorts LAST, so a default list wins only where nothing more specific priced the item. At most one list per tenant holds the flag — `prices.lists.make-default` moves it in one call.
    labels : Optional[Dict[str, Any]]
        Localised names, keyed by language tag: {&quot;de&quot;: &quot;Standardpreise&quot;, &quot;en&quot;: &quot;Standard prices&quot;}. Read the tag you need and fall back to `en`; `name` is the untranslated original.
    metadata : Optional[Dict[str, Any]]
        Free-form bag, unvalidated and never read by this app: whatever JSON object you write round-trips exactly. Its keys are the integration’s own — ERP provenance is the usual content, e.g. {&quot;source_system&quot;: &quot;erp&quot;, &quot;erp_price_group&quot;: &quot;A1&quot;}.
    name : Optional[str]
        Operator-facing name, shown wherever a human picks a list. Not addressable — integrations join on `code`.
    organization_id : Optional[str]
        Buyer scope: this list prices for buyers of this organization. Beats channel-scoped and open lists, loses to a contact-scoped one.
    priority : Optional[float]
        Tie-break WITHIN one specificity group, higher first. It never beats specificity: an organization-scoped list at priority 0 still wins over an open list at priority 100. Default 0.
    requires_auth : Optional[bool]
        Gate: when true the list resolves only for a buyer who has a contact or organization context. An anonymous resolve never matches it, so a tenant that prices only for logged-in customers flags its list and guests fall through to price-on-request rather than to some other list’s number.
    status : Optional[PriceListStatus]
        Whether the list takes part in resolution at all. Only `active` lists are candidates; `inactive` retires a list without deleting the prices it holds.
    tax_basis : Optional[PriceListTaxBasis]
        Whether the amounts stored in this list are `net` (tax excluded) or `gross` (tax included) — the one fact a price cannot be without. null inherits the tenant’s `tax_inclusive_default` setting, and the resolve answer names which of the two decided under `tax_basis_source`.
    tax_included : Optional[bool]
        LEGACY mirror of `tax_basis`. `false` is the column default, so it is NOT read as anybody having chosen net; only `true` is read as a statement (gross), and only where `tax_basis` is null. Prefer `tax_basis`.
    updated_at : Optional[str]
        When the row last changed. Written by the database, not by the caller.
    valid_from : Optional[str]
        Start of the validity window of the WHOLE list; null = open-ended. Outside the window the list is not a candidate at all. The instant compared against is the resolve call’s `at`, echoed as `basis.evaluated_at`.
    valid_until : Optional[str]
        End of the validity window of the whole list; null = open-ended. Use it to let a season expire on its own instead of deactivating a list by hand.
    """
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    code: Optional[str] = Field(default=None, alias='code')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    currency: Optional[str] = Field(default=None, alias='currency')
    description: Optional[str] = Field(default=None, alias='description')
    id: Optional[str] = Field(default=None, alias='id')
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
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
    valid_from: Optional[str] = Field(default=None, alias='valid_from')
    valid_until: Optional[str] = Field(default=None, alias='valid_until')
