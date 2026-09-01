from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Continent(AppwriteModel):
    """
    Continent

    Attributes
    ----------
    code : str
        Continent two letter code.
    name : str
        Continent name.
    """
    code: str = Field(..., alias='code')
    name: str = Field(..., alias='name')
