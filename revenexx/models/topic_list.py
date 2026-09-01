from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .topic import Topic

class TopicList(AppwriteModel):
    """
    Topic list

    Attributes
    ----------
    topics : List[Topic]
        List of topics.
    total : float
        Total number of topics that matched your query.
    """
    topics: List[Topic] = Field(..., alias='topics')
    total: float = Field(..., alias='total')
