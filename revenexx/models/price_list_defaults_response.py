from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PriceListDefaultsResponse(AppwriteModel):
    """
    What seeding found and what it had to write. Idempotent twice over: by code, and by the existence of ANY default list — so changing default_price_list_code later never produces a second default.

    Attributes
    ----------
    created : Optional[List[Any]]
        Codes of the lists this call created — empty on a tenant that was already seeded.
    existing : Optional[List[Any]]
        Codes of the lists that were already there, so nothing was written for them.
    """
    created: Optional[List[Any]] = Field(default=None, alias='created')
    existing: Optional[List[Any]] = Field(default=None, alias='existing')
