from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Variable(AppwriteModel):
    """
    Variable

    Attributes
    ----------
    createdat : str
        Variable creation date in ISO 8601 format.
    id : str
        Variable ID.
    updatedat : str
        Variable creation date in ISO 8601 format.
    key : str
        Variable key.
    resourceid : str
        ID of resource to which the variable belongs. If resourceType is &quot;project&quot;, it is empty. If resourceType is &quot;function&quot;, it is ID of the function.
    resourcetype : str
        Service to which the variable belongs. Possible values are &quot;project&quot;, &quot;function&quot;
    secret : bool
        Variable secret flag. Secret variables can only be updated or deleted, but never read.
    value : str
        Variable value.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    updatedat: str = Field(..., alias='$updatedAt')
    key: str = Field(..., alias='key')
    resourceid: str = Field(..., alias='resourceId')
    resourcetype: str = Field(..., alias='resourceType')
    secret: bool = Field(..., alias='secret')
    value: str = Field(..., alias='value')
