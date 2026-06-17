from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Error(AppwriteModel):
    """
    Uniform gateway error response.

    Attributes
    ----------
    error : bool
        Typed model field.
    message : str
        Typed model field.
    """
    error: bool = Field(..., alias='error')
    message: str = Field(..., alias='message')
