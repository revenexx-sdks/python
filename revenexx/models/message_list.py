from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .message2 import Message2

class MessageList(AppwriteModel):
    """
    Message list

    Attributes
    ----------
    messages : List[Message2]
        List of messages.
    total : float
        Total number of messages that matched your query.
    """
    messages: List[Message2] = Field(..., alias='messages')
    total: float = Field(..., alias='total')
