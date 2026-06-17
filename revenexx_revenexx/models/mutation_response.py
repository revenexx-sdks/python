from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MutationResponse(AppwriteModel):
    """
    blökkli MutationResponseLike: success flag plus the full re-materialized editor state.

    Attributes
    ----------
    state : Optional[Dict[str, Any]]
        Full editor state (see pages.editor.state).
    success : Optional[bool]
        Typed model field.
    violations : Optional[List[Any]]
        Typed model field.
    """
    state: Optional[Dict[str, Any]] = Field(default=None, alias='state')
    success: Optional[bool] = Field(default=None, alias='success')
    violations: Optional[List[Any]] = Field(default=None, alias='violations')
