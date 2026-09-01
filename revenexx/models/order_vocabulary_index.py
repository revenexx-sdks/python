from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .order_vocabulary_summary import OrderVocabularySummary

class OrderVocabularyIndex(AppwriteModel):
    """
    

    Attributes
    ----------
    app : Optional[str]
        This app&#039;s name — the part before the dot in the qualified id.
    vocabularies : Optional[List[OrderVocabularySummary]]
        Every vocabulary this app publishes, without its values — fetch one with GET /orders/vocabularies/{name}.
    """
    app: Optional[str] = Field(default=None, alias='app')
    vocabularies: Optional[List[OrderVocabularySummary]] = Field(default=None, alias='vocabularies')
