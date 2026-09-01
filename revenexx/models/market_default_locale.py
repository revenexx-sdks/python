from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.market_default_locale_source import MarketDefaultLocaleSource

class MarketDefaultLocale(AppwriteModel):
    """
    The locale a storefront should render this market in. `source` names where it came from: &#039;market&#039; (a locale flagged is_default), &#039;market_first&#039; (no flag — first by position) or &#039;tenant_fallback&#039; (the market registers none; the tenant&#039;s fallback_locale setting answered).

    Attributes
    ----------
    code : Optional[str]
        Locale code, language-COUNTRY — the language a storefront renders this market in, and the key a translation is stored under. Unique per market. The app&#039;s own seeded value is the tenant&#039;s `fallback_locale` setting, whose declared default is de-DE.
    country : Optional[str]
        ISO 3166-1 alpha-2 country code — the region half of `code`. It is a spelling of the language, not a shipping destination: a market may register de-AT without trading in Austria.
    language : Optional[str]
        ISO 639-1 language code — the language half of `code`, stored separately so a client can group markets by language without parsing.
    source : Optional[MarketDefaultLocaleSource]
        Which of the three rules answered. &#039;market&#039; — a locale of this market carries is_default. &#039;market_first&#039; — none does, so the first by position was taken. &#039;tenant_fallback&#039; — the market registers no locale at all and the tenant&#039;s fallback_locale setting answered, which means this locale is NOT one of the market&#039;s own and nothing here was configured for it.
    """
    code: Optional[str] = Field(default=None, alias='code')
    country: Optional[str] = Field(default=None, alias='country')
    language: Optional[str] = Field(default=None, alias='language')
    source: Optional[MarketDefaultLocaleSource] = Field(default=None, alias='source')
