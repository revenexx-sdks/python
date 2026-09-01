from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.shipping_vocabulary_tone import ShippingVocabularyTone

class ShippingVocabularyValue(AppwriteModel):
    """
    

    Attributes
    ----------
    description : Optional[str]
        What the value means. Either one string or a locale map keyed by locale (e.g. {en, de}) — curated copy carries the map, a value falling back to its own key carries the string.
    descriptions : Optional[Dict[str, Any]]
        Table-backed only: localized descriptions, keyed by locale.
    factor : Optional[float]
        weight-units only: kilograms per unit. A weight vocabulary without it is a list of names you cannot convert with.
    final : Optional[bool]
        The value ends the lifecycle.
    is_base : Optional[bool]
        weight-units only: the unit every other factor is expressed in.
    is_default : Optional[bool]
        Table-backed only: the value a caller falls back to, so a client can mark it without reading the settings as well.
    is_system : Optional[bool]
        Table-backed only: seeded on install. Still renameable and retirable.
    key : Optional[str]
        The value as the database stores it — what a column carries and what a filter matches. The only field a machine should compare on.
    labels : Optional[Dict[str, Any]]
        Table-backed only: localized titles, keyed by locale. Absent for a vocabulary whose values come from a CHECK constraint — those carry their copy in `title` instead.
    title : Optional[str]
        What a person reads. Falls back to a humanized key. Either one string or a locale map keyed by locale (e.g. {en, de}) — curated copy carries the map, a value falling back to its own key carries the string.
    tone : Optional[ShippingVocabularyTone]
        Semantic badge colour. The client owns what each tone looks like.
    """
    description: Optional[str] = Field(default=None, alias='description')
    descriptions: Optional[Dict[str, Any]] = Field(default=None, alias='descriptions')
    factor: Optional[float] = Field(default=None, alias='factor')
    final: Optional[bool] = Field(default=None, alias='final')
    is_base: Optional[bool] = Field(default=None, alias='is_base')
    is_default: Optional[bool] = Field(default=None, alias='is_default')
    is_system: Optional[bool] = Field(default=None, alias='is_system')
    key: Optional[str] = Field(default=None, alias='key')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    title: Optional[str] = Field(default=None, alias='title')
    tone: Optional[ShippingVocabularyTone] = Field(default=None, alias='tone')
