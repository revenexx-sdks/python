from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketTaxClassFilter(AppwriteModel):
    """
    The exact-column filters this call applied, echoed back. Every value is the raw query string, never the column&#039;s own type: `?is_default=true` comes back as `&quot;true&quot;`. A `?column=value` naming a column this entity does not have is DROPPED rather than refused — the call answers 200 with the unfiltered list, and the key missing from here is the only way to find out.

    Attributes
    ----------
    code : Optional[str]
        The `code` filter as it arrived, verbatim. Present only when the call sent it.
    created_at : Optional[str]
        The `created_at` filter as it arrived, verbatim. Present only when the call sent it. Any form the database accepts as a timestamp, including a bare date.
    id : Optional[str]
        The `id` filter as it arrived, verbatim. Present only when the call sent it.
    is_default : Optional[str]
        The `is_default` filter as it arrived, verbatim. Present only when the call sent it.
    labels : Optional[str]
        The `labels` filter as it arrived, verbatim. Present only when the call sent it.
    market_id : Optional[str]
        The owning market, taken from the route path. ALWAYS present, and always the path&#039;s market — a `?market_id=` in the query is overwritten by it rather than honoured, so this is never the value a caller sent.
    name : Optional[str]
        The `name` filter as it arrived, verbatim. Present only when the call sent it.
    position : Optional[str]
        The `position` filter as it arrived, verbatim. Present only when the call sent it.
    rate : Optional[str]
        The `rate` filter as it arrived, verbatim. Present only when the call sent it.
    updated_at : Optional[str]
        The `updated_at` filter as it arrived, verbatim. Present only when the call sent it. Any form the database accepts as a timestamp, including a bare date.
    """
    code: Optional[str] = Field(default=None, alias='code')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    is_default: Optional[str] = Field(default=None, alias='is_default')
    labels: Optional[str] = Field(default=None, alias='labels')
    market_id: Optional[str] = Field(default=None, alias='market_id')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[str] = Field(default=None, alias='position')
    rate: Optional[str] = Field(default=None, alias='rate')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
