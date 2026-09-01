from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PaymentErrorRedactRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    apply : Optional[bool]
        Write the reclassified values. Defaults to false, which reports what WOULD change and touches nothing.
    limit : Optional[float]
        How many payments to scan, oldest first. Defaults to 500, capped at 5000 — a tenant with more pre-taxonomy rows needs several runs, and re-running is free.
    """
    apply: Optional[bool] = Field(default=None, alias='apply')
    limit: Optional[float] = Field(default=None, alias='limit')
