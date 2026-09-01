from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.shipping_vocabulary_default_tone import ShippingVocabularyDefaultTone
from ..enums.shipping_vocabulary_source import ShippingVocabularySource
from .shipping_vocabulary_value import ShippingVocabularyValue

class ShippingVocabulary(AppwriteModel):
    """
    

    Attributes
    ----------
    app : Optional[str]
        The app that owns this vocabulary.
    closed : Optional[bool]
        The set is exhaustive, so a value outside it is stale data rather than a missing label. True either way — what differs is who may extend it.
    default_tone : Optional[ShippingVocabularyDefaultTone]
        The badge colour a value that names none falls back to.
    description : Optional[str]
        What the vocabulary is for. Either one string or a locale map keyed by locale (e.g. {en, de}) — curated copy carries the map, a value falling back to its own key carries the string.
    name : Optional[str]
        The vocabulary name — the part after the dot in the qualified id.
    source : Optional[ShippingVocabularySource]
        &#039;schema&#039; — the values are a CHECK constraint&#039;s, so the served set IS the enforced set. &#039;table&#039; — the values are the tenant&#039;s own rows, read per request.
    title : Optional[str]
        What the vocabulary is called. Either one string or a locale map keyed by locale (e.g. {en, de}) — curated copy carries the map, a value falling back to its own key carries the string.
    values : Optional[List[ShippingVocabularyValue]]
        Every permitted value, in the order a select should offer them — constraint order for a schema vocabulary, `position` for a table one.
    """
    app: Optional[str] = Field(default=None, alias='app')
    closed: Optional[bool] = Field(default=None, alias='closed')
    default_tone: Optional[ShippingVocabularyDefaultTone] = Field(default=None, alias='default_tone')
    description: Optional[str] = Field(default=None, alias='description')
    name: Optional[str] = Field(default=None, alias='name')
    source: Optional[ShippingVocabularySource] = Field(default=None, alias='source')
    title: Optional[str] = Field(default=None, alias='title')
    values: Optional[List[ShippingVocabularyValue]] = Field(default=None, alias='values')
