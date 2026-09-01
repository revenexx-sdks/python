from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ChannelTypeDefaults(AppwriteModel):
    """
    The same answer for the channel types, which are seeded first because the seeded channel carries one.

    Attributes
    ----------
    created : Optional[List[Any]]
        Channel type codes this call wrote. A fresh tenant gets all 5; a settled one gets none.
    existing : Optional[List[Any]]
        Seeded type codes that were already there. Note the consequence of &quot;idempotent&quot; being keyed on the code: a seeded type the merchant deliberately retired is re-created by the next call and comes back under `created`. Types the merchant added themselves are never touched.
    """
    created: Optional[List[Any]] = Field(default=None, alias='created')
    existing: Optional[List[Any]] = Field(default=None, alias='existing')
