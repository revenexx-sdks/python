from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderListKindMakeDefaultRequest(AppwriteModel):
    """
    No payload — send {}. The kind is named by the path, and there is nothing else to decide.
    """
    pass
