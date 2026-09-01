from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .form_post_submit_action import FormPostSubmitAction

T = TypeVar('T')

class FormSettings(AppwriteModel, Generic[T]):
    """
    Everything about a form that is not a field: what the storefront renders around the inputs, what happens after a successful submit, and who is told about it. Open jsonb, so an unknown key is stored and handed back rather than refused — the keys below are the ones something actually READS, and each says which reader that is. Null on a form nobody has configured, which is not an error: every one of these has a fallback.

    Attributes
    ----------
    actions : Optional[List[FormPostSubmitAction[T]]]
        What the storefront runs after a successful submit, in order. Executed by the cover BFF, not by this API — this app only stores them, and a workflow that wants the same event should listen to `form.submitted` instead.
    default_locale : Optional[str]
        The language the definition itself is written in. Read by the storefront BFF, which overlays `i18n` on top of it.
    i18n : Optional[Dict[str, Any]]
        Translations for the definition, keyed by language tag and then by field name: `{&quot;en&quot;: {&quot;email&quot;: {&quot;label&quot;: &quot;Email&quot;}}}`. Only `label`, `placeholder` and `help` are overlaid — a translation of anything else is stored and ignored. Applied by the storefront BFF before the definition reaches the browser, so the API always returns the untranslated definition.
    notify_email : Optional[str]
        This form&#039;s own notification recipient, read by THIS app at insert. It beats the tenant&#039;s `notify_email` setting; null means fall back to the tenant. The storefront never sees it — the BFF hands the browser only the submit label and the success message.
    submit_label : Optional[str]
        The submit button caption, read by the storefront. Null falls back to &#039;Submit&#039;.
    success_message : Optional[str]
        What the visitor reads after a successful submit, read by the storefront. Null falls back to a generic thank-you.
    """
    actions: Optional[List[FormPostSubmitAction[T]]] = Field(default=None, alias='actions')
    default_locale: Optional[str] = Field(default=None, alias='default_locale')
    i18n: Optional[Dict[str, Any]] = Field(default=None, alias='i18n')
    notify_email: Optional[str] = Field(default=None, alias='notify_email')
    submit_label: Optional[str] = Field(default=None, alias='submit_label')
    success_message: Optional[str] = Field(default=None, alias='success_message')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'FormSettings[T]':
        """Create FormSettings instance with typed data."""
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
