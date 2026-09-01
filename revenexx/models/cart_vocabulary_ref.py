from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.cart_vocabulary_ref_name import CartVocabularyRefName

class CartVocabularyRef(AppwriteModel):
    """
    

    Attributes
    ----------
    description : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    name : Optional[CartVocabularyRefName]
        Vocabulary name, unique within the app.
    title : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    """
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    name: Optional[CartVocabularyRefName] = Field(default=None, alias='name')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
