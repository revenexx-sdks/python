from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class SegmentRuleRecomputeAllResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    added : Optional[float]
        Rule memberships inserted across every segment in THIS call.
    done : Optional[bool]
        False when any segment is unfinished or skipped — call again.
    failed : Optional[float]
        Segments whose own recompute raised — they carry `error` and `status` in `segments` and did not abort the run.
    processed : Optional[float]
        Ruled segments the run looked at.
    removed : Optional[float]
        Rule memberships deleted across every segment in THIS call.
    segments : Optional[List[Any]]
        One entry per segment; a failed segment carries `error` and `status` instead of the counters.
    skipped : Optional[float]
        Segments the budget did not reach at all.
    """
    added: Optional[float] = Field(default=None, alias='added')
    done: Optional[bool] = Field(default=None, alias='done')
    failed: Optional[float] = Field(default=None, alias='failed')
    processed: Optional[float] = Field(default=None, alias='processed')
    removed: Optional[float] = Field(default=None, alias='removed')
    segments: Optional[List[Any]] = Field(default=None, alias='segments')
    skipped: Optional[float] = Field(default=None, alias='skipped')
