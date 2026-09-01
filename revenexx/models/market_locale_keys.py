from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketLocaleKeys(AppwriteModel):
    """
    The read and write keys for one of the market&#039;s locales, already resolved from the two settings.

    Attributes
    ----------
    code : Optional[str]
        The market&#039;s locale this entry is about.
    language : Optional[str]
        Its language part, which is also the key under language granularity.
    read : Optional[List[Any]]
        Keys to try in order until one holds text. Always starts at the exact code: a fallback fills a gap, it never outranks a stored value.
    write : Optional[str]
        A key inside a labels bag: a full locale (&#039;de-DE&#039;) under regional granularity, a bare language (&#039;de&#039;) under language granularity.
    """
    code: Optional[str] = Field(default=None, alias='code')
    language: Optional[str] = Field(default=None, alias='language')
    read: Optional[List[Any]] = Field(default=None, alias='read')
    write: Optional[str] = Field(default=None, alias='write')
