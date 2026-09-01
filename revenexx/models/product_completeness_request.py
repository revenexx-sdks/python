from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ProductCompletenessRequest(AppwriteModel):
    """
    No body. Everything this needs is the path id and what the catalog already holds; send `{}`.
    """
    pass
