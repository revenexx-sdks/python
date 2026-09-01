from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_vocabulary_tone import OrderVocabularyTone
from ..enums.order_vocabulary_name import OrderVocabularyName
from ..enums.order_vocabulary_source import OrderVocabularySource
from .order_vocabulary_value import OrderVocabularyValue

class OrderVocabulary(AppwriteModel):
    """
    

    Attributes
    ----------
    app : Optional[str]
        This app&#039;s name — the part before the dot in the qualified id.
    closed : Optional[bool]
        True when the values are the complete permitted set — always, since the routes enforce the ones the schema does not.
    default_tone : Optional[OrderVocabularyTone]
        The tone an unlabelled value gets.
    description : Optional[str]
        Either one string, or a map of locale to string ({&quot;en&quot;: …, &quot;de&quot;: …}).
    name : Optional[OrderVocabularyName]
        Which vocabulary this is — echoed from the path, and the part after the dot in the qualified id.
    source : Optional[OrderVocabularySource]
        Who enforces the set: &#039;schema&#039; = a CHECK constraint, &#039;app&#039; = the routes.
    title : Optional[str]
        Either one string, or a map of locale to string ({&quot;en&quot;: …, &quot;de&quot;: …}).
    values : Optional[List[OrderVocabularyValue]]
        Every permitted value, in CONSTRAINT order — which for a status is lifecycle order, so a client can render them as a sequence without knowing one.
    """
    app: Optional[str] = Field(default=None, alias='app')
    closed: Optional[bool] = Field(default=None, alias='closed')
    default_tone: Optional[OrderVocabularyTone] = Field(default=None, alias='default_tone')
    description: Optional[str] = Field(default=None, alias='description')
    name: Optional[OrderVocabularyName] = Field(default=None, alias='name')
    source: Optional[OrderVocabularySource] = Field(default=None, alias='source')
    title: Optional[str] = Field(default=None, alias='title')
    values: Optional[List[OrderVocabularyValue]] = Field(default=None, alias='values')
