from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Provider(AppwriteModel):
    """
    Provider

    Attributes
    ----------
    createdat : str
        Provider creation time in ISO 8601 format.
    id : str
        Provider ID.
    updatedat : str
        Provider update date in ISO 8601 format.
    credentials : Dict[str, Any]
        Provider credentials.
    enabled : bool
        Is provider enabled?
    name : str
        The name for the provider instance.
    options : Optional[Dict[str, Any]]
        Provider options.
    provider : str
        The name of the provider service.
    type : str
        Type of provider.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    updatedat: str = Field(..., alias='$updatedAt')
    credentials: Dict[str, Any] = Field(..., alias='credentials')
    enabled: bool = Field(..., alias='enabled')
    name: str = Field(..., alias='name')
    options: Optional[Dict[str, Any]] = Field(default=None, alias='options')
    provider: str = Field(..., alias='provider')
    type: str = Field(..., alias='type')
