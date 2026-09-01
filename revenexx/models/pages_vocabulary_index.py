from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.pages_vocabulary_index_app import PagesVocabularyIndexApp
from .pages_vocabulary_ref import PagesVocabularyRef

class PagesVocabularyIndex(AppwriteModel):
    """
    Which vocabularies this app publishes.

    Attributes
    ----------
    app : Optional[PagesVocabularyIndexApp]
        Always &#039;pages&#039; — the first half of the qualified id a client holds.
    vocabularies : Optional[List[PagesVocabularyRef]]
        One entry per vocabulary, without its values.
    """
    app: Optional[PagesVocabularyIndexApp] = Field(default=None, alias='app')
    vocabularies: Optional[List[PagesVocabularyRef]] = Field(default=None, alias='vocabularies')
