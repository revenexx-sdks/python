from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .cart_vocabulary_ref import CartVocabularyRef

class CartVocabularyIndex(AppwriteModel):
    """
    

    Attributes
    ----------
    app : Optional[str]
        The app that owns this vocabulary.
    vocabularies : Optional[List[CartVocabularyRef]]
        Every vocabulary this app publishes, without its values — enough to build a menu, and one call per vocabulary to fill it.
    """
    app: Optional[str] = Field(default=None, alias='app')
    vocabularies: Optional[List[CartVocabularyRef]] = Field(default=None, alias='vocabularies')
