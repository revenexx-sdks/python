from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.markets_vocabulary_summary_name import MarketsVocabularySummaryName

class MarketsVocabularySummary(AppwriteModel):
    """
    One vocabulary, enough to list it in a menu.

    Attributes
    ----------
    description : Optional[str]
        Either one string, or a map of locale to string ({&quot;en&quot;: …, &quot;de&quot;: …}).
    name : Optional[MarketsVocabularySummaryName]
        Vocabulary name, unique within the app.
    title : Optional[str]
        Either one string, or a map of locale to string ({&quot;en&quot;: …, &quot;de&quot;: …}).
    """
    description: Optional[str] = Field(default=None, alias='description')
    name: Optional[MarketsVocabularySummaryName] = Field(default=None, alias='name')
    title: Optional[str] = Field(default=None, alias='title')
