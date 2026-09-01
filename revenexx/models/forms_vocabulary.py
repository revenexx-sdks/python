from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.forms_vocabulary_tone import FormsVocabularyTone
from ..enums.forms_vocabulary_name import FormsVocabularyName
from .forms_vocabulary_value import FormsVocabularyValue

class FormsVocabulary(AppwriteModel):
    """
    

    Attributes
    ----------
    app : Optional[str]
        The app that owns this vocabulary.
    closed : Optional[bool]
        The set is exhaustive.
    default_tone : Optional[FormsVocabularyTone]
        The tone a value nobody gave one falls back to — what a badge looks like for a status that was added to the CHECK constraint before anyone styled it.
    description : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    name : Optional[FormsVocabularyName]
        Vocabulary name, unique within the app.
    source : Optional[str]
        Parsed from the CHECK constraint.
    title : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    values : Optional[List[FormsVocabularyValue]]
        Every permitted value, in constraint order — which is the order a select should offer them in, because it is the lifecycle order.
    """
    app: Optional[str] = Field(default=None, alias='app')
    closed: Optional[bool] = Field(default=None, alias='closed')
    default_tone: Optional[FormsVocabularyTone] = Field(default=None, alias='default_tone')
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    name: Optional[FormsVocabularyName] = Field(default=None, alias='name')
    source: Optional[str] = Field(default=None, alias='source')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
    values: Optional[List[FormsVocabularyValue]] = Field(default=None, alias='values')
