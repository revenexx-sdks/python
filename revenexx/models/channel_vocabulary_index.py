from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .channel_vocabulary_ref import ChannelVocabularyRef

class ChannelVocabularyIndex(AppwriteModel):
    """
    

    Attributes
    ----------
    app : Optional[str]
        The app that owns this vocabulary.
    vocabularies : Optional[List[ChannelVocabularyRef]]
        Every vocabulary this app owns, alphabetically: statuses, types, unassigned-visibility. Names only — fetch the values with GET /channels/vocabularies/{name}.
    """
    app: Optional[str] = Field(default=None, alias='app')
    vocabularies: Optional[List[ChannelVocabularyRef]] = Field(default=None, alias='vocabularies')
