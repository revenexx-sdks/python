from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.market_locale_fallback import MarketLocaleFallback
from ..enums.market_locale_granularity import MarketLocaleGranularity
from .tenant_locale_keys import TenantLocaleKeys

class TenantLocalePolicy(AppwriteModel):
    """
    How this tenant keys its translations, resolved rather than named: the key a client WRITES and the order it READS, per locale. Emitting the resolved answer is the point — a client handed only the setting names re-implements the policy and gets it subtly different, which is how a label editor came to ask for de-DE while the row held de.

    Attributes
    ----------
    fallback : Optional[MarketLocaleFallback]
        settings#locale_fallback — what a read tries after the exact key holds nothing.
    granularity : Optional[MarketLocaleGranularity]
        settings#locale_granularity — whether a value is keyed by the full locale (&#039;regional&#039;) or by its language alone.
    locales : Optional[List[TenantLocaleKeys]]
        The UNION of every market&#039;s locales, each one appearing once — the full set of inputs a tenant-baseline editor has to offer. Empty when no market registers a locale at all.
    """
    fallback: Optional[MarketLocaleFallback] = Field(default=None, alias='fallback')
    granularity: Optional[MarketLocaleGranularity] = Field(default=None, alias='granularity')
    locales: Optional[List[TenantLocaleKeys]] = Field(default=None, alias='locales')
