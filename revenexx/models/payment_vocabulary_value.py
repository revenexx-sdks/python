from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.payment_vocabulary_tone import PaymentVocabularyTone

class PaymentVocabularyValue(AppwriteModel):
    """
    One permitted value, with the words and the colour a human reads for it.

    Attributes
    ----------
    description : Optional[Dict[str, Any]]
        One sentence on what the value means, or null where the key speaks for itself. A plain string, or a locale map keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Read the requested tag, fall back to `en`.
    final : Optional[bool]
        This value ends the lifecycle — the honest way to ask &quot;is this still open?&quot; instead of matching status names.
    key : Optional[str]
        The value exactly as the database stores it — what a filter sends and what a row carries.
    title : Optional[Dict[str, Any]]
        The label to show for this value. A plain string, or a locale map keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Read the requested tag, fall back to `en`.
    tone : Optional[PaymentVocabularyTone]
        What the state MEANS, semantically: neutral, info, success, warning or danger. The client decides what each one looks like in its own design system.
    """
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    final: Optional[bool] = Field(default=None, alias='final')
    key: Optional[str] = Field(default=None, alias='key')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
    tone: Optional[PaymentVocabularyTone] = Field(default=None, alias='tone')
