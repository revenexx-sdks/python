from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderUnholdRequest(AppwriteModel):
    """
    No payload — releasing the hold is a pure state transition, and it clears hold_reason with it. Send {}.
    """
    pass
