from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.markets_vocabulary_tone import MarketsVocabularyTone

class MarketsVocabularyValue(AppwriteModel):
    """
    One permitted value, with the copy and the badge tone a client renders it as.

    Attributes
    ----------
    description : Optional[str]
        Either one string, or a map of locale to string ({&quot;en&quot;: …, &quot;de&quot;: …}).
    final : Optional[bool]
        A terminal state nothing moves out of.
    key : Optional[str]
        The value as stored in the column.
    title : Optional[str]
        Either one string, or a map of locale to string ({&quot;en&quot;: …, &quot;de&quot;: …}).
    tone : Optional[MarketsVocabularyTone]
        Semantic badge tone — the client decides what it looks like.
    """
    description: Optional[str] = Field(default=None, alias='description')
    final: Optional[bool] = Field(default=None, alias='final')
    key: Optional[str] = Field(default=None, alias='key')
    title: Optional[str] = Field(default=None, alias='title')
    tone: Optional[MarketsVocabularyTone] = Field(default=None, alias='tone')
