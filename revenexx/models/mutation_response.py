from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .editor_state import EditorState

class MutationResponse(AppwriteModel):
    """
    blökkli MutationResponseLike: whether the call was applied, plus the FULL re-materialized editor state — so a client never has to re-fetch after a change.

    Attributes
    ----------
    state : Optional[EditorState]
        Everything the blökkli editor runs on, for one page in one language, materialized at the current point of the undo history. The theme adapter maps it 1:1 onto blökkli&#039;s MappedState.
    success : Optional[bool]
        Whether the change was applied.
    violations : Optional[List[Any]]
        Why the call was refused, when `success` is false.
    """
    state: Optional[EditorState] = Field(default=None, alias='state')
    success: Optional[bool] = Field(default=None, alias='success')
    violations: Optional[List[Any]] = Field(default=None, alias='violations')
