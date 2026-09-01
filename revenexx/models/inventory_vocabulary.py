from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.inventory_vocabulary_default_tone import InventoryVocabularyDefaultTone
from ..enums.inventory_vocabulary_source import InventoryVocabularySource

class InventoryVocabulary(AppwriteModel):
    """
    

    Attributes
    ----------
    app : Optional[str]
        This app&#039;s name — the part before the dot in the qualified id.
    closed : Optional[bool]
        True when these values are the complete permitted set, because they were read out of a CHECK constraint. A value outside a closed set is therefore stale data, not a missing label — which is what lets a client show it as an error instead of inventing a title for it.
    default_tone : Optional[InventoryVocabularyDefaultTone]
        The tone a value gets when nobody has labelled it — a value added to the CHECK constraint is served with its key humanized and this tone, rather than not being served at all.
    description : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Read the requested tag, fall back to `en`.
    name : Optional[str]
        The vocabulary name, echoed — the part after the dot in the qualified id.
    source : Optional[InventoryVocabularySource]
        Where the words come from: &#039;schema&#039; — the app&#039;s own, read from the constraint. Nothing here is renameable per tenant, so a client may cache it per app version.
    title : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Read the requested tag, fall back to `en`.
    values : Optional[List[Any]]
        Every permitted value, IN CONSTRAINT ORDER — which is lifecycle order for a status, so a UI can render the steps in the order they happen.
    """
    app: Optional[str] = Field(default=None, alias='app')
    closed: Optional[bool] = Field(default=None, alias='closed')
    default_tone: Optional[InventoryVocabularyDefaultTone] = Field(default=None, alias='default_tone')
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    name: Optional[str] = Field(default=None, alias='name')
    source: Optional[InventoryVocabularySource] = Field(default=None, alias='source')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
    values: Optional[List[Any]] = Field(default=None, alias='values')
