from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_resolution_stage import OrderResolutionStage
from ..enums.order_vocabulary_tone import OrderVocabularyTone

class OrderVocabularyValue(AppwriteModel):
    """
    One permitted value with the words and the badge tone a client should render for it.

    Attributes
    ----------
    description : Optional[str]
        Either one string, or a map of locale to string ({&quot;en&quot;: …, &quot;de&quot;: …}).
    final : Optional[bool]
        True when this value ENDS the lifecycle. Lets a reader ask &quot;is this order still open?&quot; instead of matching status names it guessed.
    key : Optional[str]
        The value as stored — exactly what the CHECK constraint permits.
    stage : Optional[OrderResolutionStage]
        Only on &#039;return-resolutions&#039;: which return transition accepts this value. A settlement word on the refusal dialog is how the two sets got mixed up.
    title : Optional[str]
        Either one string, or a map of locale to string ({&quot;en&quot;: …, &quot;de&quot;: …}).
    tone : Optional[OrderVocabularyTone]
        Semantic badge colour. The client owns what each tone looks like.
    """
    description: Optional[str] = Field(default=None, alias='description')
    final: Optional[bool] = Field(default=None, alias='final')
    key: Optional[str] = Field(default=None, alias='key')
    stage: Optional[OrderResolutionStage] = Field(default=None, alias='stage')
    title: Optional[str] = Field(default=None, alias='title')
    tone: Optional[OrderVocabularyTone] = Field(default=None, alias='tone')
