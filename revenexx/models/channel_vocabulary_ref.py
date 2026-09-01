from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.channel_vocabulary_ref_name import ChannelVocabularyRefName

class ChannelVocabularyRef(AppwriteModel):
    """
    

    Attributes
    ----------
    description : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    name : Optional[ChannelVocabularyRefName]
        Vocabulary name, unique within the app.
    title : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    """
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    name: Optional[ChannelVocabularyRefName] = Field(default=None, alias='name')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
