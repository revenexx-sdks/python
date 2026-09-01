from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ReorderScanRequest(AppwriteModel):
    """
    No fields — send `{}`. What counts as low follows each row&#039;s own `reorder_point` and the market&#039;s `reorder_point_default`, exactly as GET /inventories/reorder-alerts computes it.
    """
    pass
