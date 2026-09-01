from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PrincipalResolveRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    contact_id : str
        The contact the caller is acting for.
    """
    contact_id: str = Field(..., alias='contact_id')
