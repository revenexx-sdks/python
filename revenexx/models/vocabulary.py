from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.vocabulary_default_tone import VocabularyDefaultTone
from ..enums.vocabulary_source import VocabularySource

class Vocabulary(AppwriteModel):
    """
    

    Attributes
    ----------
    app : Optional[str]
        This app&#039;s name — the part before the dot in the qualified id.
    closed : Optional[bool]
        True when the values are the complete permitted set. For a CHECK-backed vocabulary the constraint guarantees it; for a table-backed one the app refuses a value outside the rows, and for `locales` outside the configured list — the same guarantee by three mechanisms.
    default_tone : Optional[VocabularyDefaultTone]
        The tone an unlabelled value gets.
    description : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Read the requested tag, fall back to `en`. A curated label is a map; a value nobody labelled is humanized into a plain string.
    name : Optional[str]
        The vocabulary this is.
    source : Optional[VocabularySource]
        &#039;schema&#039; — a CHECK constraint owns the set. &#039;table&#039; — the tenant&#039;s own rows do. &#039;defaults&#039; — a table-backed set the tenant never wrote down, answered from the built-ins. &#039;tenant&#039; — the merchant configured the values through a setting (locales).
    title : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Read the requested tag, fall back to `en`. A curated label is a map; a value nobody labelled is humanized into a plain string.
    values : Optional[List[Any]]
        Every permitted value, in the order a select should offer them.
    """
    app: Optional[str] = Field(default=None, alias='app')
    closed: Optional[bool] = Field(default=None, alias='closed')
    default_tone: Optional[VocabularyDefaultTone] = Field(default=None, alias='default_tone')
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    name: Optional[str] = Field(default=None, alias='name')
    source: Optional[VocabularySource] = Field(default=None, alias='source')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
    values: Optional[List[Any]] = Field(default=None, alias='values')
