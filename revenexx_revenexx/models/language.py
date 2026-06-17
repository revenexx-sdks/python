from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Language(AppwriteModel):
    """
    Language

    Attributes
    ----------
    code : str
        Language two-character ISO 639-1 codes.
    name : str
        Language name.
    nativename : str
        Language native name.
    """
    code: str = Field(..., alias='code')
    name: str = Field(..., alias='name')
    nativename: str = Field(..., alias='nativeName')
