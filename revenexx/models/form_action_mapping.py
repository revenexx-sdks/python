from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class FormActionMapping(AppwriteModel):
    """
    

    Attributes
    ----------
    source : Optional[str]
        The key in the submission `data` — i.e. the `name` of a definition node.
    target : Optional[str]
        The column of the target entity it is written to.
    """
    source: Optional[str] = Field(default=None, alias='source')
    target: Optional[str] = Field(default=None, alias='target')
