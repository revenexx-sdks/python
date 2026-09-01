from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderListVocabularyIndex(AppwriteModel):
    """
    

    Attributes
    ----------
    app : Optional[str]
        The app that owns this vocabulary.
    vocabularies : Optional[List[Any]]
        Every vocabulary this app publishes, without its values — the values are one call further down, at GET /orderlists/vocabularies/{name}.
    """
    app: Optional[str] = Field(default=None, alias='app')
    vocabularies: Optional[List[Any]] = Field(default=None, alias='vocabularies')
