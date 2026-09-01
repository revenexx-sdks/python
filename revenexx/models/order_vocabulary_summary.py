from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.order_vocabulary_summary_name import OrderVocabularySummaryName

class OrderVocabularySummary(AppwriteModel):
    """
    One vocabulary, named and titled but without its values.

    Attributes
    ----------
    description : Optional[str]
        Either one string, or a map of locale to string ({&quot;en&quot;: …, &quot;de&quot;: …}).
    name : Optional[OrderVocabularySummaryName]
        Vocabulary name, unique within the app.
    title : Optional[str]
        Either one string, or a map of locale to string ({&quot;en&quot;: …, &quot;de&quot;: …}).
    """
    description: Optional[str] = Field(default=None, alias='description')
    name: Optional[OrderVocabularySummaryName] = Field(default=None, alias='name')
    title: Optional[str] = Field(default=None, alias='title')
