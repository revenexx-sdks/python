from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ShippingVocabularyIndexEntry(AppwriteModel):
    """
    One vocabulary, named and titled.

    Attributes
    ----------
    description : Optional[str]
        What the vocabulary is for. Either one string or a locale map keyed by locale (e.g. {en, de}) — curated copy carries the map, a value falling back to its own key carries the string.
    name : Optional[str]
        The part after the dot in the qualified id — what GET /shipping/vocabularies/{name} takes.
    title : Optional[str]
        What the vocabulary is called. Either one string or a locale map keyed by locale (e.g. {en, de}) — curated copy carries the map, a value falling back to its own key carries the string.
    """
    description: Optional[str] = Field(default=None, alias='description')
    name: Optional[str] = Field(default=None, alias='name')
    title: Optional[str] = Field(default=None, alias='title')
