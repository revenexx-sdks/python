from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ReservationSweepRequest(AppwriteModel):
    """
    No fields — send `{}`. The cut-off is always now, and what counts as expired follows each reservation&#039;s own `expires_at` plus the `reservation_ttl_minutes` setting of the market it belongs to.
    """
    pass
