from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketLocaleCreateRequest(AppwriteModel):
    """
    The owning market comes from the route path (&#039;market_id&#039;).

    Attributes
    ----------
    code : str
        Locale code, e.g. &#039;de-DE&#039; (unique per market).
    country : str
        ISO 3166-1 alpha-2 country code.
    is_default : Optional[bool]
        Typed model field.
    language : str
        ISO 639-1 language code.
    position : Optional[float]
        Sort position (default 0).
    """
    code: str = Field(..., alias='code')
    country: str = Field(..., alias='country')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    language: str = Field(..., alias='language')
    position: Optional[float] = Field(default=None, alias='position')
