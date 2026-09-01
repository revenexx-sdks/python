from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class CartMaintenanceRequest(AppwriteModel):
    """
    

    Attributes
    ----------
    dry_run : Optional[bool]
        Report what the sweep WOULD do and write nothing. Worth doing before a first retention run: cart_ttl_days deletes carts and their lines.
    """
    dry_run: Optional[bool] = Field(default=None, alias='dry_run')
