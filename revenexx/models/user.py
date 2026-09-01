from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .preferences import Preferences
from .target import Target

T = TypeVar('T')

class User(AppwriteModel, Generic[T]):
    """
    User

    Attributes
    ----------
    createdat : str
        User creation date in ISO 8601 format.
    id : str
        User ID.
    updatedat : str
        User update date in ISO 8601 format.
    accessedat : str
        Most recent access date in ISO 8601 format. This attribute is only updated again after 24 hours.
    email : str
        User email address.
    emailverification : bool
        Email verification status.
    hash : Optional[str]
        Password hashing algorithm.
    hashoptions : Optional[Dict[str, Any]]
        Password hashing algorithm configuration.
    labels : List[Any]
        Labels for the user.
    mfa : bool
        Multi factor authentication status.
    name : str
        User name.
    password : Optional[str]
        Hashed user password.
    passwordupdate : str
        Password update time in ISO 8601 format.
    phone : str
        User phone number in E.164 format.
    phoneverification : bool
        Phone verification status.
    prefs : Preferences[T]
        User preferences as a key-value object
    registration : str
        User registration date in ISO 8601 format.
    status : bool
        User status. Pass `true` for enabled and `false` for disabled.
    targets : List[Target]
        A user-owned message receiver. A single user may have multiple e.g. emails, phones, and a browser. Each target is registered with a single provider.
    """
    createdat: str = Field(..., alias='$createdAt')
    id: str = Field(..., alias='$id')
    updatedat: str = Field(..., alias='$updatedAt')
    accessedat: str = Field(..., alias='accessedAt')
    email: str = Field(..., alias='email')
    emailverification: bool = Field(..., alias='emailVerification')
    hash: Optional[str] = Field(default=None, alias='hash')
    hashoptions: Optional[Dict[str, Any]] = Field(default=None, alias='hashOptions')
    labels: List[Any] = Field(..., alias='labels')
    mfa: bool = Field(..., alias='mfa')
    name: str = Field(..., alias='name')
    password: Optional[str] = Field(default=None, alias='password')
    passwordupdate: str = Field(..., alias='passwordUpdate')
    phone: str = Field(..., alias='phone')
    phoneverification: bool = Field(..., alias='phoneVerification')
    prefs: Preferences[T] = Field(..., alias='prefs')
    registration: str = Field(..., alias='registration')
    status: bool = Field(..., alias='status')
    targets: List[Target] = Field(..., alias='targets')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'User[T]':
        """Create User instance with typed data."""
        instance = cls.model_validate(data)
        if 'prefs' in data and data['prefs'] is not None:
            instance.prefs = Preferences.with_data(
                data['prefs'], model_type
            )
        return instance
