from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

T = TypeVar('T')

class FormSubmissionListFilter(AppwriteModel, Generic[T]):
    """
    The exact-column filters this call was understood to carry, echoed with the values as they arrived. A query parameter that is not a filterable column of this entity is DROPPED rather than refused, and is simply missing here — so an empty object next to a query string that had a filter in it means the filter was misspelled, and is the only way to tell that from a filter that matched nothing.

    Attributes
    ----------
    created_at : Optional[str]
        The `created_at` filter, verbatim as the query string carried it. A string here whatever the column&#039;s own type.
    form_id : Optional[str]
        The `form_id` filter, verbatim as the query string carried it. A string here whatever the column&#039;s own type.
    form_slug : Optional[str]
        The `form_slug` filter, verbatim as the query string carried it. A string here whatever the column&#039;s own type.
    id : Optional[str]
        The `id` filter, verbatim as the query string carried it. A string here whatever the column&#039;s own type.
    source : Optional[str]
        The `source` filter, verbatim as the query string carried it. A string here whatever the column&#039;s own type.
    status : Optional[str]
        The `status` filter, verbatim as the query string carried it. A string here whatever the column&#039;s own type — and NOT necessarily one of the permitted values: `?status=zzz` is echoed back unchanged and matches nothing, which is the point of the echo.
    updated_at : Optional[str]
        The `updated_at` filter, verbatim as the query string carried it. A string here whatever the column&#039;s own type.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    form_id: Optional[str] = Field(default=None, alias='form_id')
    form_slug: Optional[str] = Field(default=None, alias='form_slug')
    id: Optional[str] = Field(default=None, alias='id')
    source: Optional[str] = Field(default=None, alias='source')
    status: Optional[str] = Field(default=None, alias='status')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'FormSubmissionListFilter[T]':
        """Create FormSubmissionListFilter instance with typed data."""
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
