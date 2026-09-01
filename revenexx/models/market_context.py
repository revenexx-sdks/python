from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .market_currency import MarketCurrency
from .market_default_locale import MarketDefaultLocale
from .market_locale_policy import MarketLocalePolicy
from .market_locale import MarketLocale
from .market import Market
from .market_pricing import MarketPricing
from .market_readiness import MarketReadiness
from .market_tax_class import MarketTaxClass

class MarketContext(AppwriteModel):
    """
    The whole of one market: the row, its three collections, and the four resolved answers a client would otherwise have to work out for itself.

    Attributes
    ----------
    currencies : Optional[List[MarketCurrency]]
        Every currency this market trades in, in position order. Capped at 200. The market&#039;s own base currency should be among them; readiness reports it as blocking when it is not.
    default_locale : Optional[MarketDefaultLocale]
        The locale a storefront should render this market in. `source` names where it came from: &#039;market&#039; (a locale flagged is_default), &#039;market_first&#039; (no flag — first by position) or &#039;tenant_fallback&#039; (the market registers none; the tenant&#039;s fallback_locale setting answered).
    locale_policy : Optional[MarketLocalePolicy]
        How this tenant keys its translations, resolved rather than named: the key a client WRITES and the order it READS, per locale. Emitting the resolved answer is the point — a client handed only the setting names re-implements the policy and gets it subtly different, which is how a label editor came to ask for de-DE while the row held de.
    locales : Optional[List[MarketLocale]]
        Every locale this market registers, in position order. Capped at 200. Empty is a real answer — read `default_locale` before assuming a language.
    market : Optional[Market]
        A distinct business context within a tenant — a country, a region, or a storefront segment such as B2C vs B2B — with its own base currency, locales, traded currencies and tax classes. A market is also the platform&#039;s `market` SCOPE dimension: every other commerce app slices its data by one, keyed on this row&#039;s `code`. A market is never just this row: it needs at least one locale, one currency and one tax class before it can serve, which is what /readiness measures and what /clone and /backfill build.
    pricing : Optional[MarketPricing]
        Whether a stored price in this market is NET or GROSS — the market layer of an answer the prices app also holds. A price list&#039;s own tax_basis wins over this; `tax_basis: null` with `source: &#039;unset&#039;` means this market declares nothing and the reader must fall through to the tenant&#039;s own default.
    readiness : Optional[MarketReadiness]
        Can this market actually trade? `ready` is false only when a BLOCKING check failed — no currency to quote in, no tax class to tax with. Warnings are degraded-but-serviceable.
    tax_classes : Optional[List[MarketTaxClass]]
        Every tax class of this market with its rate, in position order. Capped at 200. This is the rate table other apps resolve a line against, by code.
    """
    currencies: Optional[List[MarketCurrency]] = Field(default=None, alias='currencies')
    default_locale: Optional[MarketDefaultLocale] = Field(default=None, alias='default_locale')
    locale_policy: Optional[MarketLocalePolicy] = Field(default=None, alias='locale_policy')
    locales: Optional[List[MarketLocale]] = Field(default=None, alias='locales')
    market: Optional[Market] = Field(default=None, alias='market')
    pricing: Optional[MarketPricing] = Field(default=None, alias='pricing')
    readiness: Optional[MarketReadiness] = Field(default=None, alias='readiness')
    tax_classes: Optional[List[MarketTaxClass]] = Field(default=None, alias='tax_classes')
