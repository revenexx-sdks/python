from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class RegistrationRejectRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    decided_by : Optional[str]
        Who rejected it — recorded on the contact and carried in the event.
    reason : str
        Why the application was declined. Always stored on the contact. It only reaches the APPLICANT when the tenant&#039;s registration_reason_disclosed setting is on — the event payload then carries it, and so does the 403 the login answers.
    """
    decided_by: Optional[str] = Field(default=None, alias='decided_by')
    reason: str = Field(..., alias='reason')
