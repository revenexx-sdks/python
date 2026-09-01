from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class InventoryVocabularyIndex(AppwriteModel):
    """
    

    Attributes
    ----------
    app : Optional[str]
        This app&#039;s name — the part before the dot in a qualified vocabulary id such as `inventories.movement-types`.
    vocabularies : Optional[List[Any]]
        Every vocabulary this app publishes, WITHOUT its values — the index a client reads to discover them. Fetch the values with GET /inventories/vocabularies/{name}.
    """
    app: Optional[str] = Field(default=None, alias='app')
    vocabularies: Optional[List[Any]] = Field(default=None, alias='vocabularies')
