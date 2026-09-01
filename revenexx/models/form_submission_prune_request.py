from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.form_submission_prune_request_status import FormSubmissionPruneRequestStatus

class FormSubmissionPruneRequest(AppwriteModel):
    """
    Retention sweep. Previews unless `dry_run` is explicitly false.

    Attributes
    ----------
    dry_run : Optional[bool]
        Default TRUE. Nothing is deleted until this is explicitly false.
    form_slug : Optional[str]
        Narrow the sweep to one form.
    older_than_days : Optional[float]
        Age threshold. Omit to use the retention floor. A value BELOW the floor is raised to it — the setting is the floor, not a default, and the floor is the LONGEST submission_retention_days configured anywhere in the tenant (see the operation description).
    status : Optional[FormSubmissionPruneRequestStatus]
        Narrow the sweep to one inbox status, e.g. &#039;spam&#039;.
    """
    dry_run: Optional[bool] = Field(default=None, alias='dry_run')
    form_slug: Optional[str] = Field(default=None, alias='form_slug')
    older_than_days: Optional[float] = Field(default=None, alias='older_than_days')
    status: Optional[FormSubmissionPruneRequestStatus] = Field(default=None, alias='status')
