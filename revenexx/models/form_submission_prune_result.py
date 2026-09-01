from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .form_submission_prune_sample import FormSubmissionPruneSample

class FormSubmissionPruneResult(AppwriteModel):
    """
    

    Attributes
    ----------
    cutoff : Optional[str]
        Submissions created before this instant match. It is `now - older_than_days`, computed after the retention floor was applied, so it is the honest answer to &quot;what did this call actually consider&quot;.
    deleted : Optional[float]
        How many rows this call actually removed — always 0 on a dry run, and at most the 500-row batch size on a real one.
    dry_run : Optional[bool]
        Whether this call was a preview. True — the default — means nothing was deleted and `matched` is what a real run would take.
    floor_applied : Optional[bool]
        True when the request asked for a shorter age than the floor allows.
    matched : Optional[float]
        How many rows match, ignoring the batch size.
    older_than_days : Optional[float]
        The threshold actually applied, after the retention floor.
    remaining : Optional[float]
        Matched rows left after this batch — call again. Absent on a dry run, which deletes nothing.
    retention_days : Optional[float]
        The retention floor this sweep honoured: the LONGEST submission_retention_days configured anywhere in the tenant, baseline or market. Not the value the calling market sees — a tenant-wide sweep has to keep the longest promise anybody was given.
    retention_market : Optional[str]
        The market whose submission_retention_days set the floor — the merchant&#039;s own market CODE — or null when the tenant baseline did. It is there so a merchant can see WHY the sweep would not go younger, since the market that bound it is often not the one the request was made from.
    sample : Optional[List[FormSubmissionPruneSample]]
        Up to five matching rows (dry runs only) — id, form_slug and created_at, never the submitted data.
    """
    cutoff: Optional[str] = Field(default=None, alias='cutoff')
    deleted: Optional[float] = Field(default=None, alias='deleted')
    dry_run: Optional[bool] = Field(default=None, alias='dry_run')
    floor_applied: Optional[bool] = Field(default=None, alias='floor_applied')
    matched: Optional[float] = Field(default=None, alias='matched')
    older_than_days: Optional[float] = Field(default=None, alias='older_than_days')
    remaining: Optional[float] = Field(default=None, alias='remaining')
    retention_days: Optional[float] = Field(default=None, alias='retention_days')
    retention_market: Optional[str] = Field(default=None, alias='retention_market')
    sample: Optional[List[FormSubmissionPruneSample]] = Field(default=None, alias='sample')
