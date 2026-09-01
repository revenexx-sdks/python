from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.price_vocabulary_ref_name import PriceVocabularyRefName

class PriceVocabularyRef(AppwriteModel):
    """
    One vocabulary, named and titled — fetch its values with GET /prices/vocabularies/{name}.

    Attributes
    ----------
    description : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    name : Optional[PriceVocabularyRefName]
        Vocabulary name, unique within the app.
    title : Optional[Dict[str, Any]]
        A plain string, or a locale map keyed by language tag ({&quot;en&quot;: …, &quot;de&quot;: …}). Read the requested tag, fall back to `en`.
    """
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    name: Optional[PriceVocabularyRefName] = Field(default=None, alias='name')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
