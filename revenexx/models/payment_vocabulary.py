from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.payment_vocabulary_tone import PaymentVocabularyTone
from .payment_vocabulary_value import PaymentVocabularyValue

class PaymentVocabulary(AppwriteModel):
    """
    One enum this app owns, with every permitted value.

    Attributes
    ----------
    app : Optional[str]
        The app that owns this vocabulary — always `payments` here. Together with `name` it forms the platform-wide key `payments.statuses`.
    closed : Optional[bool]
        True when the set comes from a CHECK constraint and is therefore exhaustive — a client may treat anything outside it as stale data rather than a missing label.
    default_tone : Optional[PaymentVocabularyTone]
        The tone a permitted value nobody labelled falls back to, so every value is renderable.
    description : Optional[Dict[str, Any]]
        What this set of values is about. A plain string, or a locale map keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Read the requested tag, fall back to `en`.
    name : Optional[str]
        The vocabulary name, as it appears in the URL.
    source : Optional[str]
        Where the values come from. `schema` means they were parsed out of the CHECK constraint, so what is served is what the database enforces.
    title : Optional[Dict[str, Any]]
        The vocabulary&#039;s own label, for a filter heading or a column title. A plain string, or a locale map keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Read the requested tag, fall back to `en`.
    values : Optional[List[PaymentVocabularyValue]]
        Every permitted value, in constraint order — which is the lifecycle order an author wrote, and the order a select should offer.
    """
    app: Optional[str] = Field(default=None, alias='app')
    closed: Optional[bool] = Field(default=None, alias='closed')
    default_tone: Optional[PaymentVocabularyTone] = Field(default=None, alias='default_tone')
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    name: Optional[str] = Field(default=None, alias='name')
    source: Optional[str] = Field(default=None, alias='source')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
    values: Optional[List[PaymentVocabularyValue]] = Field(default=None, alias='values')
