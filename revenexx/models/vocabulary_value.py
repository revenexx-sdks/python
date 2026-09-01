from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.vocabulary_tone import VocabularyTone

class VocabularyValue(AppwriteModel):
    """
    

    Attributes
    ----------
    description : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Read the requested tag, fall back to `en`.
    final : Optional[bool]
        A terminal state — nothing moves out of it. False or absent on a vocabulary that is not a lifecycle.
    key : Optional[str]
        The value as it is STORED and as the CHECK admits it — what a filter or a write sends.
    title : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Read the requested tag, fall back to `en`.
    tone : Optional[VocabularyTone]
        Which badge colour a UI should paint this value in.
    """
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    final: Optional[bool] = Field(default=None, alias='final')
    key: Optional[str] = Field(default=None, alias='key')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
    tone: Optional[VocabularyTone] = Field(default=None, alias='tone')
