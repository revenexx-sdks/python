from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.price_vocabulary_tone import PriceVocabularyTone
from ..enums.price_vocabulary_name import PriceVocabularyName
from ..enums.price_vocabulary_source import PriceVocabularySource
from .price_vocabulary_value import PriceVocabularyValue

class PriceVocabulary(AppwriteModel):
    """
    One closed value set with the words a human reads for it — so a UI never keeps its own copy of an enum this app enforces.

    Attributes
    ----------
    app : Optional[str]
        The app that owns this vocabulary.
    closed : Optional[bool]
        Always true here: the values come from a CHECK constraint, so the list is exhaustive and a value outside it is stale data rather than a missing label.
    default_tone : Optional[PriceVocabularyTone]
        The tone a value that carries none falls back to.
    description : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    name : Optional[PriceVocabularyName]
        Vocabulary name, unique within the app.
    source : Optional[PriceVocabularySource]
        Where the values came from. &#039;schema&#039; = a CHECK constraint in this app&#039;s own schema.json.
    title : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    values : Optional[List[PriceVocabularyValue]]
        Every permitted value, in CHECK-constraint order — which is the order an author wrote and the order a select should offer.
    """
    app: Optional[str] = Field(default=None, alias='app')
    closed: Optional[bool] = Field(default=None, alias='closed')
    default_tone: Optional[PriceVocabularyTone] = Field(default=None, alias='default_tone')
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    name: Optional[PriceVocabularyName] = Field(default=None, alias='name')
    source: Optional[PriceVocabularySource] = Field(default=None, alias='source')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
    values: Optional[List[PriceVocabularyValue]] = Field(default=None, alias='values')
