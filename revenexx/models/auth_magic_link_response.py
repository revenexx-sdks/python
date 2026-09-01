from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.auth_mail_source import AuthMailSource

T = TypeVar('T')

class AuthMagicLinkResponse(AppwriteModel, Generic[T]):
    """
    The token, minus its secret. The secret travels only in the mailed link — a caller holding both would not need the mail at all.

    Attributes
    ----------
    id : Optional[str]
        The token that was created.
    expire : Optional[str]
        When the link stops working. The mail says the same in words.
    mail : Optional[AuthMailSource]
        Which template the buyer received: &#039;tenant&#039; is this shop&#039;s own, &#039;platform&#039; the identity service&#039;s built-in one — the fallback when messaging could not be reached. The value is the same either way, so the flow works in both cases.
    userid : Optional[str]
        The platform user it belongs to — new when the address was.
    """
    id: Optional[str] = Field(default=None, alias='$id')
    expire: Optional[str] = Field(default=None, alias='expire')
    mail: Optional[AuthMailSource] = Field(default=None, alias='mail')
    userid: Optional[str] = Field(default=None, alias='userId')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'AuthMagicLinkResponse[T]':
        """Create AuthMagicLinkResponse instance with typed data."""
        internal_fields = {k: v for k, v in data.items() if k.startswith('$')}
        user_data = {k: v for k, v in data.items() if not k.startswith('$')}
        instance = cls.model_validate(internal_fields)
        instance._data = model_type(**user_data) if model_type is not dict else user_data
        return instance

    _data: Any = PrivateAttr(default_factory=dict)

    @property
    def data(self) -> T:
        return cast(T, self._data)

    @data.setter
    def data(self, value: T) -> None:
        object.__setattr__(self, '_data', value)

    def to_dict(self) -> Dict[str, Any]:
        result = super().to_dict()
        if hasattr(self, '_data'):
            if isinstance(self._data, dict):
                result['data'] = self._data
            elif hasattr(self._data, 'model_dump'):
                result['data'] = self._data.model_dump(mode='json')
            else:
                result['data'] = self._data
        return result
