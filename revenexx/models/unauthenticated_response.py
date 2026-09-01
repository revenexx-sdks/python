from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class UnauthenticatedResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    message : Optional[str]
        Typed model field.
    """
    message: Optional[str] = Field(default=None, alias='message')
