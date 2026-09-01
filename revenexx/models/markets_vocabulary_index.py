from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .markets_vocabulary_summary import MarketsVocabularySummary

class MarketsVocabularyIndex(AppwriteModel):
    """
    Every closed value set this app owns, by name — enough to build a menu of them without fetching each one.

    Attributes
    ----------
    app : Optional[str]
        The app that owns this vocabulary.
    vocabularies : Optional[List[MarketsVocabularySummary]]
        Every vocabulary this app publishes, named and titled but without its values — fetch one by name for those.
    """
    app: Optional[str] = Field(default=None, alias='app')
    vocabularies: Optional[List[MarketsVocabularySummary]] = Field(default=None, alias='vocabularies')
