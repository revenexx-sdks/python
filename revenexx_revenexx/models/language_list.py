from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .language import Language

class LanguageList(AppwriteModel):
    """
    Languages List

    Attributes
    ----------
    languages : List[Language]
        List of languages.
    total : float
        Total number of languages that matched your query.
    """
    languages: List[Language] = Field(..., alias='languages')
    total: float = Field(..., alias='total')
