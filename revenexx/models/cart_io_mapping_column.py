from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CartIoMappingColumn(AppwriteModel):
    """
    

    Attributes
    ----------
    xfrom : str
        The cart or line field, spelled as this app spells it — one of the canonical column names.
    to : str
        What that field is called on the outside: the CSV header, or the JSON key of the system on the other end.
    """
    xfrom: str = Field(..., alias='from')
    to: str = Field(..., alias='to')
