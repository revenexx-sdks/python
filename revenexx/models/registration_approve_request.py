from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class RegistrationApproveRequest(AppwriteModel):
    """
    No required fields — send {}.

    Attributes
    ----------
    decided_by : Optional[str]
        Who approved it — recorded on the contact and carried in the event. Free text (operator id or email); this app does not resolve it.
    """
    decided_by: Optional[str] = Field(default=None, alias='decided_by')
