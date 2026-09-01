from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .price_resolve_item import PriceResolveItem

class PriceResolveRequest(AppwriteModel):
    """
    Buyer context + items. Unpriceable items come back as on_request — a missing price is a first-class state, never 0.

    Attributes
    ----------
    at : Optional[str]
        The instant every validity window — list and entry — is evaluated at (ISO 8601). Default now. This is how a promo price is previewed before it starts, and it is echoed as `basis.evaluated_at`.
    channel_id : Optional[str]
        Buyer context: the sales channel. Third scope — beats the open lists, loses to contact and organization.
    contact_id : Optional[str]
        Buyer context: the contact this quote is for. The most specific scope — a list naming this contact beats every other list, whatever their priority. Sending it (or organization_id) is also what makes the buyer AUTHENTICATED for `requires_auth` lists and for the tenant’s anonymous_resolve_allowed setting.
    currency : Optional[str]
        ISO 4217 code the quote is wanted in. ONLY lists in this currency are candidates and nothing is ever converted, so a wrong value here is not a rounding difference — it is no price at all. Omit to take the buyer market’s currency, then the tenant’s default_currency; `basis.currency_source` names which applied.
    items : List[PriceResolveItem]
        Items to price, at most 200 per call — a whole cart or a whole product listing in one round trip. The answer holds one entry per item, in this order.
    market_id : Optional[str]
        Buyer context: the market, as a uuid pin for older callers. Prefer the `X-Revenexx-Market` header, which carries a market CODE and is what scopes the visible price lists. The market decides the tax rates AND which per-market settings (rounding, tie-break, anonymous access) apply — with several markets and no signal at all the answer says `tax.resolved: false`, `reason: market_required` rather than quoting another market’s VAT.
    organization_id : Optional[str]
        Buyer context: the organization the buyer belongs to. Second most specific scope; also counts as authenticated.
    """
    at: Optional[str] = Field(default=None, alias='at')
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    currency: Optional[str] = Field(default=None, alias='currency')
    items: List[PriceResolveItem] = Field(..., alias='items')
    market_id: Optional[str] = Field(default=None, alias='market_id')
    organization_id: Optional[str] = Field(default=None, alias='organization_id')
