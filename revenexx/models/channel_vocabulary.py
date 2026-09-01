from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.channel_vocabulary_tone import ChannelVocabularyTone
from ..enums.channel_vocabulary_name import ChannelVocabularyName
from ..enums.channel_vocabulary_source import ChannelVocabularySource
from .channel_vocabulary_value import ChannelVocabularyValue

class ChannelVocabulary(AppwriteModel):
    """
    

    Attributes
    ----------
    app : Optional[str]
        The app that owns this vocabulary.
    closed : Optional[bool]
        Always true: the set is exhaustive at this moment, so a value outside it is stale data rather than a missing label. For a table-backed vocabulary that is a statement about now, not forever — the tenant may add to it.
    default_tone : Optional[ChannelVocabularyTone]
        The tone a value that carries none falls back to.
    description : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    name : Optional[ChannelVocabularyName]
        Vocabulary name, unique within the app.
    source : Optional[ChannelVocabularySource]
        Who owns the value set. &#039;schema&#039; = a CHECK constraint in this app&#039;s own schema.json; &#039;table&#039; = the tenant&#039;s own rows.
    title : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    values : Optional[List[ChannelVocabularyValue]]
        Every permitted value, in author order — the order a select should offer, not alphabetical. For a CHECK-backed vocabulary that is the constraint&#039;s own order; for the table-backed `types` it is the tenant&#039;s `position` order.
    """
    app: Optional[str] = Field(default=None, alias='app')
    closed: Optional[bool] = Field(default=None, alias='closed')
    default_tone: Optional[ChannelVocabularyTone] = Field(default=None, alias='default_tone')
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    name: Optional[ChannelVocabularyName] = Field(default=None, alias='name')
    source: Optional[ChannelVocabularySource] = Field(default=None, alias='source')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
    values: Optional[List[ChannelVocabularyValue]] = Field(default=None, alias='values')
