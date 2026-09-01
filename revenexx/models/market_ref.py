from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketRef(AppwriteModel):
    """
    The market that was read from, resolved — so a caller who passed a code back gets the uuid, and one who passed a uuid gets the code the rest of the platform stores.

    Attributes
    ----------
    code : Optional[str]
        The source market&#039;s code — the value other apps scope by.
    id : Optional[str]
        The source market&#039;s primary key.
    """
    code: Optional[str] = Field(default=None, alias='code')
    id: Optional[str] = Field(default=None, alias='id')
