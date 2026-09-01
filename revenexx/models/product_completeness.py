from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ProductCompleteness(AppwriteModel):
    """
    What was measured and stored into `products.completeness` by this call — how much of what the family requires the product actually carries.

    Attributes
    ----------
    computed_at : Optional[str]
        When this measurement was taken. It is a snapshot: editing the product does not update it, the next `POST /products/{id}/completeness` does.
    filled : Optional[float]
        How many of those carry a value — in ANY bucket, so a name held only in German counts.
    missing : Optional[List[Any]]
        Attribute codes with no value in any bucket.
    ratio : Optional[float]
        filled / required, 0..1. A family that requires nothing is 1, not undefined.
    required : Optional[float]
        Attributes the product&#039;s family marks is_required.
    """
    computed_at: Optional[str] = Field(default=None, alias='computed_at')
    filled: Optional[float] = Field(default=None, alias='filled')
    missing: Optional[List[Any]] = Field(default=None, alias='missing')
    ratio: Optional[float] = Field(default=None, alias='ratio')
    required: Optional[float] = Field(default=None, alias='required')
