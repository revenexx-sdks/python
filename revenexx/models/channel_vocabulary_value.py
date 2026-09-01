from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.channel_vocabulary_tone import ChannelVocabularyTone

class ChannelVocabularyValue(AppwriteModel):
    """
    

    Attributes
    ----------
    description : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    descriptions : Optional[Dict[str, Any]]
        Table-backed vocabularies only: the localized descriptions. A locale map keyed by language tag: {&quot;en&quot;: …, &quot;de&quot;: …}. Read the requested tag and fall back to the plain column beside it.
    final : Optional[bool]
        The value ends the lifecycle.
    is_default : Optional[bool]
        Table-backed vocabularies only: the value a create falls back to.
    is_system : Optional[bool]
        Table-backed vocabularies only: seeded on install rather than added by the tenant. Still renameable and retirable.
    key : Optional[str]
        The value as the database stores and enforces it.
    labels : Optional[Dict[str, Any]]
        Table-backed vocabularies only: the localized titles. `title` stays the fallback. A locale map keyed by language tag: {&quot;en&quot;: …, &quot;de&quot;: …}. Read the requested tag and fall back to the plain column beside it.
    title : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    tone : Optional[ChannelVocabularyTone]
        Semantic badge colour. The client owns what each tone looks like.
    """
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    descriptions: Optional[Dict[str, Any]] = Field(default=None, alias='descriptions')
    final: Optional[bool] = Field(default=None, alias='final')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    is_system: Optional[bool] = Field(default=None, alias='is_system')
    key: Optional[str] = Field(default=None, alias='key')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
    tone: Optional[ChannelVocabularyTone] = Field(default=None, alias='tone')
