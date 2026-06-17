from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .contact import Contact

class AuthRegisterResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    contact : Optional[Contact]
        Typed model field.
    user_id : Optional[str]
        Typed model field.
    """
    contact: Optional[Contact] = Field(default=None, alias='contact')
    user_id: Optional[str] = Field(default=None, alias='user_id')
