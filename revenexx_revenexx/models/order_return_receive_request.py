from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OrderReturnReceiveRequest(AppwriteModel):
    """
    No payload — receiving is a pure state transition (registered → received).
    """
    pass
