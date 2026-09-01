from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class NumberRange(AppwriteModel):
    """
    A counter that issues human-readable numbers, one per series: orders, delivery notes, returns. The format is {prefix}{counter padded to padding}{suffix}, and drawing a number moves the counter.

    Attributes
    ----------
    channel_id : Optional[str]
        The sales channel this range was created for, as a label. It does NOT select the range: a draw finds the range by `code` alone, and the unique index (tenant, code) means one code is one range per tenant — so an order on another channel draws from the same range this one names. Null on the three seeded ranges, which is every tenant-wide range.
    code : Optional[str]
        Which counter this is, in the app&#039;s own words: &#039;order&#039; numbers orders, &#039;delivery&#039; numbers delivery notes, &#039;return&#039; numbers returns. Unique per tenant, and the value the order_number_range_code / delivery_number_range_code / return_number_range_code settings point at — a setting naming a code no range carries is the 422 &#039;number_range_missing&#039;.
    counter : Optional[float]
        The last number DRAWN — state, not configuration. The next draw is counter + step and writes the new value back, so moving this forward skips numbers and moving it back re-issues them (and the unique index then answers 409).
    created_at : Optional[str]
        When the range was created.
    id : Optional[str]
        Primary key of the number range.
    metadata : Optional[Dict[str, Any]]
        Free-form data for the caller. This app stores it and returns it, and reads nothing out of it.
    padding : Optional[float]
        How wide the counter is written, zero-padded: 6 makes 123 into 000123. 0 writes the bare number. Widening it later does not renumber what was already drawn.
    position_step : Optional[float]
        The gap between the position numbers of a new order: 10 numbers the lines 10, 20, 30 — room to slot a line in between later without renumbering the rest. Read from the ORDER range only.
    prefix : Optional[str]
        Literal text in front of the counter: &#039;ORD-&#039; turns counter 123 into ORD-000123. Empty by default.
    step : Optional[float]
        How far the counter moves per draw. 1 is consecutive numbering; a larger step is what a merchant chooses who does not want their order volume readable off an invoice.
    suffix : Optional[str]
        Literal text after the counter — a market or year marker on merchants who number that way. Empty by default, which is what most of them use.
    updated_at : Optional[str]
        When the range last changed — which includes every single number draw, because a draw writes the counter.
    """
    channel_id: Optional[str] = Field(default=None, alias='channel_id')
    code: Optional[str] = Field(default=None, alias='code')
    counter: Optional[float] = Field(default=None, alias='counter')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    id: Optional[str] = Field(default=None, alias='id')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    padding: Optional[float] = Field(default=None, alias='padding')
    position_step: Optional[float] = Field(default=None, alias='position_step')
    prefix: Optional[str] = Field(default=None, alias='prefix')
    step: Optional[float] = Field(default=None, alias='step')
    suffix: Optional[str] = Field(default=None, alias='suffix')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
