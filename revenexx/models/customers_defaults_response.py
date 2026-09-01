from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CustomersDefaultsResponse(AppwriteModel):
    """
    

    Attributes
    ----------
    sets : Optional[Dict[str, Any]]
        One entry per value set, keyed by its route name — `payment-terms`, `address-types`, `lifecycle-stages`, `contact-event-kinds`. Each says what THIS call did: `created` are the codes it inserted, `existing` the seeded codes it found already there and left completely alone (a merchant&#039;s rename included). A second call therefore answers with everything under `existing` and nothing under `created`.
    """
    sets: Optional[Dict[str, Any]] = Field(default=None, alias='sets')
