from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketMakeDefaultRequest(AppwriteModel):
    """
    No payload — send {}. Which market is promoted comes from the path, and there is nothing else to say.
    """
    pass
