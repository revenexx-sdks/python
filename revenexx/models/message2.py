from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.message2_status import Message2Status

class Message2(AppwriteModel):
    """
    Message

    Attributes
    ----------
    createdat : str
        Message creation time in ISO 8601 format.
    id : str
        Message ID.
    updatedat : str
        Message update date in ISO 8601 format.
    data : Dict[str, Any]
        Data of the message.
    deliveredat : Optional[str]
        The time when the message was delivered.
    deliveredtotal : float
        Number of recipients the message was delivered to.
    deliveryerrors : Optional[List[Any]]
        Delivery errors if any.
    providertype : str
        Message provider type.
    scheduledat : Optional[str]
        The scheduled time for message.
    status : Message2Status
        Status of delivery.
    targets : List[Any]
        Target IDs set as recipients.
    topics : List[Any]
        Topic IDs set as recipients.
    users : List[Any]
        User IDs set as recipients.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    updatedat: str = Field(..., alias='$updatedAt')
    data: Dict[str, Any] = Field(..., alias='data')
    deliveredat: Optional[str] = Field(default=None, alias='deliveredAt')
    deliveredtotal: float = Field(..., alias='deliveredTotal')
    deliveryerrors: Optional[List[Any]] = Field(default=None, alias='deliveryErrors')
    providertype: str = Field(..., alias='providerType')
    scheduledat: Optional[str] = Field(default=None, alias='scheduledAt')
    status: Message2Status = Field(..., alias='status')
    targets: List[Any] = Field(..., alias='targets')
    topics: List[Any] = Field(..., alias='topics')
    users: List[Any] = Field(..., alias='users')
