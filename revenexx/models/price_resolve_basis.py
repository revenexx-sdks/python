from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.price_currency_source import PriceCurrencySource
from ..enums.price_list_tiebreak import PriceListTiebreak
from ..enums.price_rounding_mode import PriceRoundingMode
from ..enums.price_tax_inclusive_default import PriceTaxInclusiveDefault

class PriceResolveBasis(AppwriteModel):
    """
    The policy this answer was computed under — the tenant settings in force plus where the currency came from.

    Attributes
    ----------
    anonymous_resolve_allowed : Optional[bool]
        false ⇒ a buyer with no contact/organization is answered on_request for everything.
    currency_source : Optional[PriceCurrencySource]
        Where `currency` came from: the request, the buyer market&#039;s own currency, the tenant&#039;s default_currency setting, or the shipped fallback.
    evaluated_at : Optional[str]
        The instant validity windows were evaluated at.
    price_list_priority_tiebreak : Optional[PriceListTiebreak]
        Which list won where specificity and priority tied.
    price_precision : Optional[float]
        Decimals every DERIVED amount (net, gross, line totals) was rounded to.
    rounding_mode : Optional[PriceRoundingMode]
        How those amounts landed on the last decimal.
    tax_inclusive_default : Optional[PriceTaxInclusiveDefault]
        Tenant setting: the basis a price list that states none is read on.
    """
    anonymous_resolve_allowed: Optional[bool] = Field(default=None, alias='anonymous_resolve_allowed')
    currency_source: Optional[PriceCurrencySource] = Field(default=None, alias='currency_source')
    evaluated_at: Optional[str] = Field(default=None, alias='evaluated_at')
    price_list_priority_tiebreak: Optional[PriceListTiebreak] = Field(default=None, alias='price_list_priority_tiebreak')
    price_precision: Optional[float] = Field(default=None, alias='price_precision')
    rounding_mode: Optional[PriceRoundingMode] = Field(default=None, alias='rounding_mode')
    tax_inclusive_default: Optional[PriceTaxInclusiveDefault] = Field(default=None, alias='tax_inclusive_default')
