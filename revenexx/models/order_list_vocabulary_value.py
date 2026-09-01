from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_list_vocabulary_tone import OrderListVocabularyTone

class OrderListVocabularyValue(AppwriteModel):
    """
    

    Attributes
    ----------
    description : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    descriptions : Optional[Dict[str, Any]]
        Localized descriptions of a tenant-owned value, keyed by locale.
    final : Optional[bool]
        The value ends the lifecycle. Always false for `kinds` — a list kind is not a state.
    is_default : Optional[bool]
        The value a create falls back to, so a client can mark it without reading the settings as well.
    is_system : Optional[bool]
        Seeded on install rather than created by the tenant. Still renameable and retirable.
    key : Optional[str]
        The value as the database stores and enforces it — for `kinds`, the `code` a list carries.
    labels : Optional[Dict[str, Any]]
        Localized titles of a tenant-owned value, keyed by locale.
    title : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    tone : Optional[OrderListVocabularyTone]
        Semantic badge colour. The client owns what each tone looks like.
    """
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    descriptions: Optional[Dict[str, Any]] = Field(default=None, alias='descriptions')
    final: Optional[bool] = Field(default=None, alias='final')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    is_system: Optional[bool] = Field(default=None, alias='is_system')
    key: Optional[str] = Field(default=None, alias='key')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
    tone: Optional[OrderListVocabularyTone] = Field(default=None, alias='tone')
