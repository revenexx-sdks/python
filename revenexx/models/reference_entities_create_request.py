from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ReferenceEntitiesCreateRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    code : str
        The entity&#039;s stable identifier — a domain of records the catalog POINTS AT instead of duplicating, so a brand is edited once and not on nine thousand products. Unique per tenant.
    image : Optional[str]
        A delivery path or URL for the entity&#039;s own icon. Cosmetic — nothing in this app resolves it.
    labels : Optional[Dict[str, Any]]
        What the entity is called, per language tag — the heading over its record list.
    """
    code: str = Field(..., alias='code')
    image: Optional[str] = Field(default=None, alias='image')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
