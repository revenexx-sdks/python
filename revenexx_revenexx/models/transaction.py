from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Transaction(AppwriteModel):
    """
    Transaction

    Attributes
    ----------
    createdat : str
        Transaction creation time in ISO 8601 format.
    id : str
        Transaction ID.
    updatedat : str
        Transaction update date in ISO 8601 format.
    expiresat : str
        Expiration time in ISO 8601 format.
    operations : float
        Number of operations in the transaction.
    status : str
        Current status of the transaction. One of: pending, committing, committed, rolled_back, failed.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    updatedat: str = Field(..., alias='$updatedAt')
    expiresat: str = Field(..., alias='expiresAt')
    operations: float = Field(..., alias='operations')
    status: str = Field(..., alias='status')
