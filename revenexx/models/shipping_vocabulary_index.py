from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .shipping_vocabulary_index_entry import ShippingVocabularyIndexEntry

class ShippingVocabularyIndex(AppwriteModel):
    """
    

    Attributes
    ----------
    app : Optional[str]
        The app that owns these vocabularies — the part before the dot in a qualified id.
    vocabularies : Optional[List[ShippingVocabularyIndexEntry]]
        Every vocabulary this app publishes, without its values. Names only: fetch one to get the set.
    """
    app: Optional[str] = Field(default=None, alias='app')
    vocabularies: Optional[List[ShippingVocabularyIndexEntry]] = Field(default=None, alias='vocabularies')
