from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.market_status import MarketStatus

class MarketUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    code : Optional[str]
        Market code, unique per tenant, and the single most load-bearing string in this app: it IS the market scope slug. The Entity Scoping Engine publishes it as the `market` dimension (`scope_context.market` in the JWT), and every other commerce app — products, prices, orders, customers — stores THIS value to say which market a row belongs to. Renaming it re-keys that scope for everyone, so treat it as permanent. Accepted in place of the uuid on /readiness, /clone, /backfill and /make-default — but not on the item routes or /context, which take a uuid only.
    currency : Optional[str]
        Base currency this market quotes in — ISO 4217, and schema.json&#039;s own default is &#039;EUR&#039;. This is the single currency prices are STATED in; the currencies collection under the market is the wider set it accepts. A base currency missing from that collection is a blocking readiness failure.
    is_default : Optional[bool]
        The tenant default market — what a call naming no market falls back to. Exactly one market holds it; move it with POST /markets/{id}/make-default rather than by writing this flag, which does not demote the market that currently holds it.
    labels : Optional[Dict[str, Any]]
        Localized display names for storefronts, keyed by locale: a flat {locale: label} map, one level deep, string values. WHICH key to write is not free — GET /markets/{id}/context returns `locale_policy`, whose `write` is the key this tenant keys by (a full locale under regional granularity, a bare language under language granularity) and whose `read` is the order to try. Null means nothing is translated and `name` is all there is.
    name : Optional[str]
        Display name, in the operator&#039;s own language. Cockpit copy only — nothing resolves a market by it.
    position : Optional[float]
        Sort position among the tenant&#039;s markets, ascending, default 0. Presentation only — it decides the order the Cockpit and a market picker list them in, and nothing resolves a market by it.
    status : Optional[MarketStatus]
        Default &#039;active&#039;. Only an active market serves a storefront; &#039;inactive&#039; keeps the market and all its configuration but takes it out of service. Readiness reports an active market that cannot trade as `serving: true, ready: false` — live and broken.
    """
    code: Optional[str] = Field(default=None, alias='code')
    currency: Optional[str] = Field(default=None, alias='currency')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    status: Optional[MarketStatus] = Field(default=None, alias='status')
