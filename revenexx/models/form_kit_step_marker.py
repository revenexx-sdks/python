from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

T = TypeVar('T')

class FormKitStepMarker(AppwriteModel, Generic[T]):
    """
    A Revenexx step marker. The storefront cuts the flat array at each marker and renders the nodes that follow it as one wizard step, then removes the marker before FormKit renders anything. A definition with no marker is a single-step form.

    Attributes
    ----------
    id : Optional[str]
        Stable id for the step, so a client can address it.
    kind : Optional[str]
        What the step is: &#039;fields&#039; for a normal step, &#039;thankyou&#039; for the confirmation panel shown after a successful submit.
    title : Optional[str]
        The step heading the visitor reads.
    """
    id: Optional[str] = Field(default=None, alias='id')
    kind: Optional[str] = Field(default=None, alias='kind')
    title: Optional[str] = Field(default=None, alias='title')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'FormKitStepMarker[T]':
        """Create FormKitStepMarker instance with typed data."""
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
