from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketLocaleUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    code : Optional[str]
        Locale code, language-COUNTRY — the language a storefront renders this market in, and the key a translation is stored under. Unique per market. The app&#039;s own seeded value is the tenant&#039;s `fallback_locale` setting, whose declared default is de-DE.
    country : Optional[str]
        ISO 3166-1 alpha-2 country code — the region half of `code`. It is a spelling of the language, not a shipping destination: a market may register de-AT without trading in Austria.
    is_default : Optional[bool]
        The locale a storefront renders this market in when the request asks for none. At most one per market; where none carries the flag the first by position is used, and `default_locale.source` on the context says which of the two happened.
    language : Optional[str]
        ISO 639-1 language code — the language half of `code`, stored separately so a client can group markets by language without parsing.
    position : Optional[float]
        Sort position among this market&#039;s locales, ascending, default 0 — and the tie-break that picks a default when no locale is flagged.
    """
    code: Optional[str] = Field(default=None, alias='code')
    country: Optional[str] = Field(default=None, alias='country')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    language: Optional[str] = Field(default=None, alias='language')
    position: Optional[float] = Field(default=None, alias='position')
