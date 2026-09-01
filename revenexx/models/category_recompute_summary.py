from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CategoryRecomputeSummary(AppwriteModel):
    """
    

    Attributes
    ----------
    added : Optional[float]
        Membership rows inserted with source=&#039;rule&#039; by this call.
    batched : Optional[bool]
        False → the bulk insert was refused and the call fell back to one request per row. A performance fact, not an error.
    category_id : Optional[str]
        The category this pass belongs to, echoed back — a caller driving several loops keys its state by it.
    code : Optional[str]
        The category&#039;s code, so a nightly log names something a person recognises.
    computed_at : Optional[str]
        When the pass completed, and what `categories.rules_computed_at` was stamped with. Null while `done` is false.
    cursor : Optional[str]
        The product id this call reconciled up to, to hand back on the next one. Null when `done`.
    done : Optional[bool]
        False → this call spent its budget mid-pass. Send `cursor` back to continue; the counters below are THIS call only, so a caller looping to completion sums them itself.
    error : Optional[str]
        Present instead of the counters when this category failed.
    processed : Optional[float]
        Matching products examined by this call.
    removed : Optional[float]
        Stale rule rows deleted by this call.
    skipped : Optional[bool]
        True → the budget ran out before this category was reached; it carries no counters.
    status : Optional[float]
        The HTTP status this category WOULD have answered on its own — 400 for a rule that does not compile, 404 for one that vanished mid-run. Null when it succeeded.
    total : Optional[float]
        Products the rule currently selects. Null while `done` is false — the pass has not seen the whole catalog yet, so there is no total to report.
    """
    added: Optional[float] = Field(default=None, alias='added')
    batched: Optional[bool] = Field(default=None, alias='batched')
    category_id: Optional[str] = Field(default=None, alias='category_id')
    code: Optional[str] = Field(default=None, alias='code')
    computed_at: Optional[str] = Field(default=None, alias='computed_at')
    cursor: Optional[str] = Field(default=None, alias='cursor')
    done: Optional[bool] = Field(default=None, alias='done')
    error: Optional[str] = Field(default=None, alias='error')
    processed: Optional[float] = Field(default=None, alias='processed')
    removed: Optional[float] = Field(default=None, alias='removed')
    skipped: Optional[bool] = Field(default=None, alias='skipped')
    status: Optional[float] = Field(default=None, alias='status')
    total: Optional[float] = Field(default=None, alias='total')
