from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.cart_vocabulary_tone import CartVocabularyTone
from ..enums.cart_vocabulary_name import CartVocabularyName
from ..enums.cart_vocabulary_source import CartVocabularySource
from .cart_vocabulary_value import CartVocabularyValue

class CartVocabulary(AppwriteModel):
    """
    

    Attributes
    ----------
    app : Optional[str]
        The app that owns this vocabulary.
    closed : Optional[bool]
        Always true here: the values come from a CHECK constraint, so the list is exhaustive and a value outside it is stale data rather than a missing label.
    default_tone : Optional[CartVocabularyTone]
        The tone a value that carries none falls back to.
    description : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    name : Optional[CartVocabularyName]
        Vocabulary name, unique within the app.
    source : Optional[CartVocabularySource]
        Where the values came from. &#039;schema&#039; = a CHECK constraint in this app&#039;s own schema.json.
    title : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    values : Optional[List[CartVocabularyValue]]
        Every permitted value, in the order the CHECK constraint lists them — which is the order a select should offer them in.
    """
    app: Optional[str] = Field(default=None, alias='app')
    closed: Optional[bool] = Field(default=None, alias='closed')
    default_tone: Optional[CartVocabularyTone] = Field(default=None, alias='default_tone')
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    name: Optional[CartVocabularyName] = Field(default=None, alias='name')
    source: Optional[CartVocabularySource] = Field(default=None, alias='source')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
    values: Optional[List[CartVocabularyValue]] = Field(default=None, alias='values')
