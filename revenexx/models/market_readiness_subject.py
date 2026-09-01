from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.market_status import MarketStatus

class MarketReadinessSubject(AppwriteModel):
    """
    The market the verdict is about, identified rather than returned in full — the five columns a reader needs to know which market answered. Read GET /markets/{id} for the rest.

    Attributes
    ----------
    code : Optional[str]
        Market code, unique per tenant, and the single most load-bearing string in this app: it IS the market scope slug. The Entity Scoping Engine publishes it as the `market` dimension (`scope_context.market` in the JWT), and every other commerce app — products, prices, orders, customers — stores THIS value to say which market a row belongs to. Renaming it re-keys that scope for everyone, so treat it as permanent. Accepted in place of the uuid on /readiness, /clone, /backfill and /make-default — but not on the item routes or /context, which take a uuid only.
    currency : Optional[str]
        Base currency this market quotes in — ISO 4217, and schema.json&#039;s own default is &#039;EUR&#039;. This is the single currency prices are STATED in; the currencies collection under the market is the wider set it accepts. A base currency missing from that collection is a blocking readiness failure.
    id : Optional[str]
        The market&#039;s primary key — resolved, so a call that named the market by its code gets the uuid back.
    name : Optional[str]
        Display name, in the operator&#039;s own language. Cockpit copy only — nothing resolves a market by it.
    status : Optional[MarketStatus]
        Default &#039;active&#039;. Only an active market serves a storefront; &#039;inactive&#039; keeps the market and all its configuration but takes it out of service. Readiness reports an active market that cannot trade as `serving: true, ready: false` — live and broken.
    """
    code: Optional[str] = Field(default=None, alias='code')
    currency: Optional[str] = Field(default=None, alias='currency')
    id: Optional[str] = Field(default=None, alias='id')
    name: Optional[str] = Field(default=None, alias='name')
    status: Optional[MarketStatus] = Field(default=None, alias='status')
