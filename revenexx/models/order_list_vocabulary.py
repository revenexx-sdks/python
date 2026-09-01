from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_list_vocabulary_default_tone import OrderListVocabularyDefaultTone
from ..enums.order_list_vocabulary_name import OrderListVocabularyName
from ..enums.order_list_vocabulary_source import OrderListVocabularySource
from .order_list_vocabulary_value import OrderListVocabularyValue

class OrderListVocabulary(AppwriteModel):
    """
    

    Attributes
    ----------
    app : Optional[str]
        The app that owns this vocabulary.
    closed : Optional[bool]
        The set is exhaustive: a value outside it is stale data, not a missing label.
    default_tone : Optional[OrderListVocabularyDefaultTone]
        The badge colour a value carries when it names none of its own.
    description : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    name : Optional[OrderListVocabularyName]
        Vocabulary name, unique within the app.
    source : Optional[OrderListVocabularySource]
        &#039;schema&#039; — a CHECK constraint owns the set; &#039;table&#039; — the tenant&#039;s own rows do.
    title : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    values : Optional[List[OrderListVocabularyValue]]
        Every permitted value, in the order a select should offer them.
    """
    app: Optional[str] = Field(default=None, alias='app')
    closed: Optional[bool] = Field(default=None, alias='closed')
    default_tone: Optional[OrderListVocabularyDefaultTone] = Field(default=None, alias='default_tone')
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    name: Optional[OrderListVocabularyName] = Field(default=None, alias='name')
    source: Optional[OrderListVocabularySource] = Field(default=None, alias='source')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
    values: Optional[List[OrderListVocabularyValue]] = Field(default=None, alias='values')
