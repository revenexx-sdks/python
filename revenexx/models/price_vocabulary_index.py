from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .price_vocabulary_ref import PriceVocabularyRef

class PriceVocabularyIndex(AppwriteModel):
    """
    What this app publishes, without the values — one fetch a UI can cache and then pull only the vocabularies it renders.

    Attributes
    ----------
    app : Optional[str]
        The app that owns this vocabulary.
    vocabularies : Optional[List[PriceVocabularyRef]]
        Every vocabulary this app owns, sorted by name.
    """
    app: Optional[str] = Field(default=None, alias='app')
    vocabularies: Optional[List[PriceVocabularyRef]] = Field(default=None, alias='vocabularies')
