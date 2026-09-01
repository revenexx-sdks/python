from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.validation_failed_response_status import ValidationFailedResponseStatus

class ValidationFailedResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    errors : Optional[List[Any]]
        Typed model field.
    status : Optional[ValidationFailedResponseStatus]
        Typed model field.
    """
    errors: Optional[List[Any]] = Field(default=None, alias='errors')
    status: Optional[ValidationFailedResponseStatus] = Field(default=None, alias='status')
