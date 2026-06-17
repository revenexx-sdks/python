from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketLocaleUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    code : Optional[str]
        Locale code, e.g. &#039;de-DE&#039; (unique per market).
    country : Optional[str]
        ISO 3166-1 alpha-2 country code.
    is_default : Optional[bool]
        Typed model field.
    language : Optional[str]
        ISO 639-1 language code.
    position : Optional[float]
        Sort position (default 0).
    """
    code: Optional[str] = Field(default=None, alias='code')
    country: Optional[str] = Field(default=None, alias='country')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    language: Optional[str] = Field(default=None, alias='language')
    position: Optional[float] = Field(default=None, alias='position')
