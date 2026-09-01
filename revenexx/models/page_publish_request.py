from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PagePublishRequest(AppwriteModel):
    """
    What to record about this publication.

    Attributes
    ----------
    force : Optional[bool]
        Publish despite violations. Without it a page with unresolved violations answers 422 and nothing is written.
    label : Optional[str]
        What to call this publication in the page&#039;s history — &quot;Autumn campaign&quot; rather than a timestamp.
    """
    force: Optional[bool] = Field(default=None, alias='force')
    label: Optional[str] = Field(default=None, alias='label')
