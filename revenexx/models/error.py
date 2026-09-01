from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Error(AppwriteModel):
    """
    Uniform error response. The same shape is emitted by the gateway and by the apps behind it, so one parser covers the whole API.

    Attributes
    ----------
    code : Optional[str]
        Machine-readable discriminator, e.g. not_found, invalid_value, unique_violation.
    error : str
        Human-readable message. Was a boolean on gateway-emitted errors before; it is a string everywhere now.
    message : Optional[str]
        Deprecated duplicate of `error`, kept so existing readers keep working. Read `error`.
    """
    code: Optional[str] = Field(default=None, alias='code')
    error: str = Field(..., alias='error')
    message: Optional[str] = Field(default=None, alias='message')
