from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class BulkJobType(AppwriteModel):
    """
    One value per PE-102 block that moves data.
    """
    pass
