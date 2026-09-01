from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .price_resolve_basis import PriceResolveBasis
from .resolved_price import ResolvedPrice
from .price_tax_context import PriceTaxContext

class PriceResolveResponse(AppwriteModel):
    """
    One answer per requested item, in request order, plus the currency, the tax context and the policy the numbers were computed under.

    Attributes
    ----------
    basis : Optional[PriceResolveBasis]
        The policy this answer was computed under — the tenant settings in force plus where the currency came from.
    currency : Optional[str]
        ISO 4217 currency the whole answer is quoted in, and the currency lists had to match to be candidates at all. `basis.currency_source` says where it came from: the request, the buyer market, the tenant setting, or the shipped fallback.
    prices : Optional[List[ResolvedPrice]]
        One entry per requested item, in the order the items were sent. An item that could not be priced is present and `on_request`, never missing.
    tax : Optional[PriceTaxContext]
        Tax resolution status of this answer. resolved=false ⇒ tax_class/tax_rate are unknown, NOT zero.
    """
    basis: Optional[PriceResolveBasis] = Field(default=None, alias='basis')
    currency: Optional[str] = Field(default=None, alias='currency')
    prices: Optional[List[ResolvedPrice]] = Field(default=None, alias='prices')
    tax: Optional[PriceTaxContext] = Field(default=None, alias='tax')
