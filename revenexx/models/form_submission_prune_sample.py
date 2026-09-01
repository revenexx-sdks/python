from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class FormSubmissionPruneSample(AppwriteModel):
    """
    One row the sweep would delete, shown so a merchant can recognise what is at stake before turning the preview off. Three columns only — never the submitted data.

    Attributes
    ----------
    created_at : Optional[str]
        When it arrived — the age this sweep is judging it on.
    form_slug : Optional[str]
        The form&#039;s slug as it stood when this submission arrived, copied onto the row: the inbox filters by form without a join, and a submission still says which form collected it after that form has been renamed. It does not outlive a DELETED form — the foreign key cascades and takes the submission with it. On a write the body&#039;s value WINS; omit it and the form&#039;s own slug is copied in.
    id : Optional[str]
        The submission that would be deleted. Fetch it with GET /v1/forms/submissions/{id} to see what it holds.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    form_slug: Optional[str] = Field(default=None, alias='form_slug')
    id: Optional[str] = Field(default=None, alias='id')
