from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.form_notify_source import FormNotifySource

T = TypeVar('T')

class FormSubmissionMetadata(AppwriteModel, Generic[T]):
    """
    Free-form metadata, plus what this app stamped on at insert. The recipient is resolved ONCE, here, because this row is the payload of `form.submitted` — a workflow reads the address off the event instead of re-resolving a form&#039;s settings that may since have changed.

    Attributes
    ----------
    notify_email : Optional[str]
        The resolved notification recipient, or null when neither the form nor the tenant names one.
    notify_source : Optional[FormNotifySource]
        Which of the two configured recipients won: the form&#039;s own, or the tenant setting.
    spam_reason : Optional[str]
        Present only on a submission the honeypot caught: &#039;honeypot&#039;.
    """
    notify_email: Optional[str] = Field(default=None, alias='notify_email')
    notify_source: Optional[FormNotifySource] = Field(default=None, alias='notify_source')
    spam_reason: Optional[str] = Field(default=None, alias='spam_reason')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'FormSubmissionMetadata[T]':
        """Create FormSubmissionMetadata instance with typed data."""
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
