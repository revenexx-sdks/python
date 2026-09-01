from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PageUserSettingsRequest(AppwriteModel):
    """
    The preferences to store for the calling user.

    Attributes
    ----------
    settings : Optional[Dict[str, Any]]
        The whole preferences bag — replaced, not merged, so send all of it. Its keys vary by the editor build and this app reads none of them. Null or omitted stores `{}`, which is how a user resets their editor.
    """
    settings: Optional[Dict[str, Any]] = Field(default=None, alias='settings')
