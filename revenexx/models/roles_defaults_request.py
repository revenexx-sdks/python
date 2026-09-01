from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class RolesDefaultsRequest(AppwriteModel):
    """
    No fields — send {}.
    """
    pass
