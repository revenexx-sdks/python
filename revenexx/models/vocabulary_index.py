from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class VocabularyIndex(AppwriteModel):
    """
    

    Attributes
    ----------
    app : Optional[str]
        This app&#039;s name — the part before the dot in the qualified id `customers.&lt;name&gt;`.
    vocabularies : Optional[List[Any]]
        Every vocabulary this app publishes, without their values.
    """
    app: Optional[str] = Field(default=None, alias='app')
    vocabularies: Optional[List[Any]] = Field(default=None, alias='vocabularies')
