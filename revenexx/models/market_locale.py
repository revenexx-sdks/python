from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketLocale(AppwriteModel):
    """
    One language a market is rendered in, and one key its translations are stored under. A market may register several; one of them is the default a storefront falls back to.

    Attributes
    ----------
    code : Optional[str]
        Locale code, language-COUNTRY — the language a storefront renders this market in, and the key a translation is stored under. Unique per market. The app&#039;s own seeded value is the tenant&#039;s `fallback_locale` setting, whose declared default is de-DE.
    country : Optional[str]
        ISO 3166-1 alpha-2 country code — the region half of `code`. It is a spelling of the language, not a shipping destination: a market may register de-AT without trading in Austria.
    created_at : Optional[str]
        When the locale was registered on this market. Set by the database; never writable.
    id : Optional[str]
        Primary key of this locale registration. The locale is named by `code` everywhere else.
    is_default : Optional[bool]
        The locale a storefront renders this market in when the request asks for none. At most one per market; where none carries the flag the first by position is used, and `default_locale.source` on the context says which of the two happened.
    language : Optional[str]
        ISO 639-1 language code — the language half of `code`, stored separately so a client can group markets by language without parsing.
    market_id : Optional[str]
        The market this locale belongs to. Filled from the route path on write and never read out of the body; ON DELETE CASCADE, so deleting the market deletes this row.
    position : Optional[float]
        Sort position among this market&#039;s locales, ascending, default 0 — and the tie-break that picks a default when no locale is flagged.
    """
    code: Optional[str] = Field(default=None, alias='code')
    country: Optional[str] = Field(default=None, alias='country')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    language: Optional[str] = Field(default=None, alias='language')
    market_id: Optional[str] = Field(default=None, alias='market_id')
    position: Optional[float] = Field(default=None, alias='position')
