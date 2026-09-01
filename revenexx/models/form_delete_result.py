from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.form_status import FormStatus

class FormDeleteResult(AppwriteModel):
    """
    

    Attributes
    ----------
    archived : Optional[bool]
        True when the policy is &#039;archive&#039; and submissions exist — the form was archived, not deleted.
    deleted : Optional[bool]
        The form row was removed — and with it, via the cascade, every submission it had. `submissions` below says how many went, and they are not recoverable.
    id : Optional[str]
        The form in the path.
    status : Optional[FormStatus]
        The form&#039;s status after the call. Only present on the archive branch.
    submissions : Optional[float]
        How many submissions the form had when the call was weighed — and therefore, when `deleted` is true, how many were deleted with it. The whole inbox, across every market: the cascade is a database operation and takes them all, so an active `X-Revenexx-Market` does not narrow this number.
    """
    archived: Optional[bool] = Field(default=None, alias='archived')
    deleted: Optional[bool] = Field(default=None, alias='deleted')
    id: Optional[str] = Field(default=None, alias='id')
    status: Optional[FormStatus] = Field(default=None, alias='status')
    submissions: Optional[float] = Field(default=None, alias='submissions')
