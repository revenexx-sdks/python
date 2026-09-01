from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class SegmentRuleRecomputeResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    added : Optional[float]
        Rule memberships inserted by THIS call.
    batched : Optional[bool]
        True when every membership insert used a bulk array request; false if any batch fell back to row-at-a-time.
    computed_at : Optional[str]
        Set when the pass completes.
    cursor : Optional[str]
        Send back on the next call; null when the pass is done.
    done : Optional[bool]
        False means work remains — POST again with `cursor`.
    processed : Optional[float]
        Matching organizations examined by THIS call.
    removed : Optional[float]
        Rule memberships deleted by THIS call.
    segment_id : Optional[str]
        The segment that was recomputed.
    total : Optional[float]
        The rule&#039;s full match count; null until done.
    """
    added: Optional[float] = Field(default=None, alias='added')
    batched: Optional[bool] = Field(default=None, alias='batched')
    computed_at: Optional[str] = Field(default=None, alias='computed_at')
    cursor: Optional[str] = Field(default=None, alias='cursor')
    done: Optional[bool] = Field(default=None, alias='done')
    processed: Optional[float] = Field(default=None, alias='processed')
    removed: Optional[float] = Field(default=None, alias='removed')
    segment_id: Optional[str] = Field(default=None, alias='segment_id')
    total: Optional[float] = Field(default=None, alias='total')
