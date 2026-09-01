from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .form_action_mapping import FormActionMapping

T = TypeVar('T')

class FormPostSubmitAction(AppwriteModel, Generic[T]):
    """
    One post-submit action. `webhook` POSTs `{form, source, data}` to `url`; `entity` writes the mapped fields into another app&#039;s entity; `event` is a no-op, because `form.submitted` already carries it.

    Attributes
    ----------
    app : Optional[str]
        Entity actions: the app that owns the target entity, e.g. &#039;crm&#039;.
    enabled : Optional[bool]
        Disabled actions are skipped. An action with no flag is not run.
    entity : Optional[str]
        Entity actions: the entity to write, e.g. &#039;contacts&#039;.
    mapping : Optional[List[FormActionMapping]]
        Entity actions: which submitted value becomes which column — `{&quot;source&quot;: &quot;email&quot;, &quot;target&quot;: &quot;email&quot;}` reads `data.email` and writes it to the target&#039;s `email`.
    method : Optional[str]
        Webhook actions: the HTTP method. Defaults to POST.
    path : Optional[str]
        Entity actions: an explicit route to POST to, instead of the one built from `app` and `entity`.
    type : Optional[str]
        Which action this is: &#039;webhook&#039;, &#039;entity&#039; or &#039;event&#039;.
    url : Optional[str]
        Webhook actions: where to POST. It is called with an 8 second timeout and its answer is not shown to the visitor.
    """
    app: Optional[str] = Field(default=None, alias='app')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    entity: Optional[str] = Field(default=None, alias='entity')
    mapping: Optional[List[FormActionMapping]] = Field(default=None, alias='mapping')
    method: Optional[str] = Field(default=None, alias='method')
    path: Optional[str] = Field(default=None, alias='path')
    type: Optional[str] = Field(default=None, alias='type')
    url: Optional[str] = Field(default=None, alias='url')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'FormPostSubmitAction[T]':
        """Create FormPostSubmitAction instance with typed data."""
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
