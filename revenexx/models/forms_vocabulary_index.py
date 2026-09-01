from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .forms_vocabulary_summary import FormsVocabularySummary

class FormsVocabularyIndex(AppwriteModel):
    """
    

    Attributes
    ----------
    app : Optional[str]
        The app that owns this vocabulary.
    vocabularies : Optional[List[FormsVocabularySummary]]
        Every vocabulary this app publishes, without its values — enough to build a menu, not enough to fill a select. Fetch one by name for that.
    """
    app: Optional[str] = Field(default=None, alias='app')
    vocabularies: Optional[List[FormsVocabularySummary]] = Field(default=None, alias='vocabularies')
