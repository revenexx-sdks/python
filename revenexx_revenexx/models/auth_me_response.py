from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .contact import Contact

class AuthMeResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    contact : Optional[Contact]
        Typed model field.
    user : Optional[Dict[str, Any]]
        Typed model field.
    """
    contact: Optional[Contact] = Field(default=None, alias='contact')
    user: Optional[Dict[str, Any]] = Field(default=None, alias='user')
