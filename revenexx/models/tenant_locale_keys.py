from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class TenantLocaleKeys(AppwriteModel):
    """
    One locale somewhere in this tenant, its read and write keys, and the markets that asked for it.

    Attributes
    ----------
    code : Optional[str]
        The locale this entry is about, as some market registered it.
    language : Optional[str]
        Its language part, which is also the key under language granularity.
    markets : Optional[List[Any]]
        Codes of the markets that registered this locale, sorted — who a baseline translation written here is actually for. An editor that lists six inputs without saying who needs them invites translations nobody will ever read.
    read : Optional[List[Any]]
        Keys to try in order until one holds text — the same resolved order the per-market answer gives, so a baseline value and a market value can never be keyed differently.
    write : Optional[str]
        A key inside a labels bag: a full locale (&#039;de-DE&#039;) under regional granularity, a bare language (&#039;de&#039;) under language granularity.
    """
    code: Optional[str] = Field(default=None, alias='code')
    language: Optional[str] = Field(default=None, alias='language')
    markets: Optional[List[Any]] = Field(default=None, alias='markets')
    read: Optional[List[Any]] = Field(default=None, alias='read')
    write: Optional[str] = Field(default=None, alias='write')
