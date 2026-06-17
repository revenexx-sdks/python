from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .preferences import Preferences

T = TypeVar('T')

class Team(AppwriteModel, Generic[T]):
    """
    Team

    Attributes
    ----------
    createdat : str
        Team creation date in ISO 8601 format.
    id : str
        Team ID.
    updatedat : str
        Team update date in ISO 8601 format.
    name : str
        Team name.
    prefs : Preferences[T]
        Team preferences as a key-value object
    total : float
        Total number of team members.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    prefs: Preferences[T] = Field(..., alias='prefs')
    total: float = Field(..., alias='total')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'Team[T]':
        """Create Team instance with typed data."""
        instance = cls.model_validate(data)
        if 'prefs' in data and data['prefs'] is not None:
            instance.prefs = Preferences.with_data(
                data['prefs'], model_type
            )
        return instance
