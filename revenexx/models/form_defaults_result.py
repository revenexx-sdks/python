from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class FormDefaultsResult(AppwriteModel):
    """
    

    Attributes
    ----------
    created : Optional[List[Any]]
        Slugs this call created. On a tenant that has had the app installed for more than a moment this is empty — the sample form is seeded on `app.installed`.
    existing : Optional[List[Any]]
        Slugs that were already there and were left alone. Nothing about them was overwritten — a form the merchant has edited stays edited.
    """
    created: Optional[List[Any]] = Field(default=None, alias='created')
    existing: Optional[List[Any]] = Field(default=None, alias='existing')
