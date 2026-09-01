from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.pages_vocabulary_tone import PagesVocabularyTone

class PagesVocabularyValue(AppwriteModel):
    """
    One permitted value of a vocabulary, with everything needed to render it.

    Attributes
    ----------
    description : Optional[Dict[str, Any]]
        When to use this value, or null when nobody wrote one. A plain string, or a locale map keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Read the requested tag, fall back to `en`.
    final : Optional[bool]
        The value ends the lifecycle.
    key : Optional[str]
        The value as the database stores and enforces it.
    title : Optional[Dict[str, Any]]
        What a person reads. Falls back to a humanized key. A plain string, or a locale map keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Read the requested tag, fall back to `en`.
    tone : Optional[PagesVocabularyTone]
        Semantic badge colour. The client owns what each tone looks like.
    """
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    final: Optional[bool] = Field(default=None, alias='final')
    key: Optional[str] = Field(default=None, alias='key')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
    tone: Optional[PagesVocabularyTone] = Field(default=None, alias='tone')
