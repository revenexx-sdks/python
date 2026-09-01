from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.markets_vocabulary_tone import MarketsVocabularyTone
from ..enums.markets_vocabulary_name import MarketsVocabularyName
from ..enums.markets_vocabulary_source import MarketsVocabularySource
from .markets_vocabulary_value import MarketsVocabularyValue

class MarketsVocabulary(AppwriteModel):
    """
    One closed value set this app owns, parsed out of the CHECK constraint in schema.json — the served set IS the enforced set. `closed: true` means a client may treat anything outside `values` as stale data.

    Attributes
    ----------
    app : Optional[str]
        The app that owns this vocabulary.
    closed : Optional[bool]
        Always true here: the values come from a CHECK constraint, so the list is exhaustive.
    default_tone : Optional[MarketsVocabularyTone]
        The tone a value that carries none falls back to.
    description : Optional[str]
        Either one string, or a map of locale to string ({&quot;en&quot;: …, &quot;de&quot;: …}).
    name : Optional[MarketsVocabularyName]
        Vocabulary name, unique within the app.
    source : Optional[MarketsVocabularySource]
        Where the values came from. &#039;schema&#039; = a CHECK constraint in this app&#039;s own schema.json.
    title : Optional[str]
        Either one string, or a map of locale to string ({&quot;en&quot;: …, &quot;de&quot;: …}).
    values : Optional[List[MarketsVocabularyValue]]
        Every value the column may hold, in the order the CHECK constraint lists them — which is the order a select box should offer them in. Exhaustive, because `closed` is true.
    """
    app: Optional[str] = Field(default=None, alias='app')
    closed: Optional[bool] = Field(default=None, alias='closed')
    default_tone: Optional[MarketsVocabularyTone] = Field(default=None, alias='default_tone')
    description: Optional[str] = Field(default=None, alias='description')
    name: Optional[MarketsVocabularyName] = Field(default=None, alias='name')
    source: Optional[MarketsVocabularySource] = Field(default=None, alias='source')
    title: Optional[str] = Field(default=None, alias='title')
    values: Optional[List[MarketsVocabularyValue]] = Field(default=None, alias='values')
