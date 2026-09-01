from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.pages_vocabulary_app import PagesVocabularyApp
from ..enums.pages_vocabulary_tone import PagesVocabularyTone
from ..enums.pages_vocabulary_name import PagesVocabularyName
from ..enums.pages_vocabulary_source import PagesVocabularySource
from .pages_vocabulary_value import PagesVocabularyValue

class PagesVocabulary(AppwriteModel):
    """
    One vocabulary and every value it permits.

    Attributes
    ----------
    app : Optional[PagesVocabularyApp]
        Always &#039;pages&#039;.
    closed : Optional[bool]
        The set is exhaustive, so a value outside it is stale data rather than a missing label.
    default_tone : Optional[PagesVocabularyTone]
        The badge colour a value nobody toned falls back to.
    description : Optional[Dict[str, Any]]
        What the set is for, or null. A plain string, or a locale map keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Read the requested tag, fall back to `en`.
    name : Optional[PagesVocabularyName]
        The vocabulary name, echoed.
    source : Optional[PagesVocabularySource]
        Always &#039;schema&#039; — the values are parsed from the column&#039;s CHECK constraint, which is why the served set cannot drift from the enforced one.
    title : Optional[Dict[str, Any]]
        What this set of values is called. A plain string, or a locale map keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Read the requested tag, fall back to `en`.
    values : Optional[List[PagesVocabularyValue]]
        Every permitted value, in the order the constraint lists them — which is the order a select should offer.
    """
    app: Optional[PagesVocabularyApp] = Field(default=None, alias='app')
    closed: Optional[bool] = Field(default=None, alias='closed')
    default_tone: Optional[PagesVocabularyTone] = Field(default=None, alias='default_tone')
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    name: Optional[PagesVocabularyName] = Field(default=None, alias='name')
    source: Optional[PagesVocabularySource] = Field(default=None, alias='source')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
    values: Optional[List[PagesVocabularyValue]] = Field(default=None, alias='values')
