from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Country(AppwriteModel):
    """
    Country

    Attributes
    ----------
    code : str
        Country two-character ISO 3166-1 alpha code.
    name : str
        Country name.
    """
    code: str = Field(..., alias='code')
    name: str = Field(..., alias='name')
