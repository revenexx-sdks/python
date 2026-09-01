from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class FormSubmissionDeleteResult(AppwriteModel):
    """
    

    Attributes
    ----------
    deleted : Optional[bool]
        Always true — the row is gone. A submission that was not there answers 404 instead, so this is never false.
    id : Optional[str]
        The submission that was removed, echoed from the path.
    """
    deleted: Optional[bool] = Field(default=None, alias='deleted')
    id: Optional[str] = Field(default=None, alias='id')
