from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.price_vocabulary_tone import PriceVocabularyTone

class PriceVocabularyValue(AppwriteModel):
    """
    One permitted value, with its words and its badge tone.

    Attributes
    ----------
    description : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    final : Optional[bool]
        The value ends the lifecycle.
    key : Optional[str]
        The value as the database stores and enforces it.
    title : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    tone : Optional[PriceVocabularyTone]
        Semantic badge colour. The client owns what each tone looks like.
    """
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    final: Optional[bool] = Field(default=None, alias='final')
    key: Optional[str] = Field(default=None, alias='key')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
    tone: Optional[PriceVocabularyTone] = Field(default=None, alias='tone')
