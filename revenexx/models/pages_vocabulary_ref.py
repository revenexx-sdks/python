from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PagesVocabularyRef(AppwriteModel):
    """
    One vocabulary, named but not unpacked.

    Attributes
    ----------
    description : Optional[Dict[str, Any]]
        What the set is for, or null. A plain string, or a locale map keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Read the requested tag, fall back to `en`.
    name : Optional[str]
        The name to fetch it by — the part after the dot in the qualified id.
    title : Optional[Dict[str, Any]]
        What this set of values is called. A plain string, or a locale map keyed by language tag ({ &quot;en&quot;: …, &quot;de&quot;: … }). Read the requested tag, fall back to `en`.
    """
    description: Optional[Dict[str, Any]] = Field(default=None, alias='description')
    name: Optional[str] = Field(default=None, alias='name')
    title: Optional[Dict[str, Any]] = Field(default=None, alias='title')
