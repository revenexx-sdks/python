from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderNumberRangeCreateRequest(AppwriteModel):
    """
    Number pattern: &#039;{prefix}{counter padded to padding}{suffix}&#039;.

    Attributes
    ----------
    channel_id : Optional[str]
        Typed model field.
    code : str
        Range key drawn by the app (&#039;order&#039;, &#039;delivery&#039;, &#039;return&#039;) — unique per tenant.
    counter : Optional[float]
        Current counter value (default 0) — the next number draws counter+step.
    metadata : Optional[Dict[str, Any]]
        Free-form metadata.
    padding : Optional[float]
        Zero-padding width of the counter (default 6).
    position_step : Optional[float]
        Position numbering increment for order items (default 10).
    prefix : Optional[str]
        Default &#039;&#039;.
    step : Optional[float]
        Counter increment per drawn number (default 1).
    suffix : Optional[str]
        Default &#039;&#039;.
    """
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    code: str = Field(..., alias='code')
    counter: Optional[float] = Field(default=None, alias='counter')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    padding: Optional[float] = Field(default=None, alias='padding')
    position_step: Optional[float] = Field(default=None, alias='position_step')
    prefix: Optional[str] = Field(default=None, alias='prefix')
    step: Optional[float] = Field(default=None, alias='step')
    suffix: Optional[str] = Field(default=None, alias='suffix')
