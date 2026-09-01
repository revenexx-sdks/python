from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

T = TypeVar('T')

class SearchParameters(AppwriteModel, Generic[T]):
    """
    Typesense search parameters. Only the commonly used ones are enumerated — the proxy forwards the whole object, so any parameter Typesense accepts may be sent.

    Attributes
    ----------
    exclude_fields : Optional[str]
        Comma-separated document fields to omit.
    facet_by : Optional[str]
        Comma-separated fields to facet on.
    filter_by : Optional[str]
        Filter expression, e.g. `in_stock:=true &amp;&amp; price:&lt;100`. ANDed with the tenant filter the proxy injects.
    group_by : Optional[str]
        Comma-separated fields to group results by.
    highlight_full_fields : Optional[str]
        Comma-separated fields to highlight in full.
    include_fields : Optional[str]
        Comma-separated document fields to return.
    max_facet_values : Optional[float]
        Facet values to return per field.
    num_typos : Optional[float]
        Typos tolerated per query token.
    page : Optional[float]
        1-based page number.
    per_page : Optional[float]
        Hits per page.
    prefix : Optional[str]
        Whether the last token is a prefix; per-field when comma-separated.
    q : Optional[str]
        Query text. Use `*` to match everything.
    query_by : Optional[str]
        Comma-separated fields to search, in weight order.
    sort_by : Optional[str]
        Sort expression, e.g. `price:desc`.
    """
    exclude_fields: Optional[str] = Field(default=None, alias='exclude_fields')
    facet_by: Optional[str] = Field(default=None, alias='facet_by')
    filter_by: Optional[str] = Field(default=None, alias='filter_by')
    group_by: Optional[str] = Field(default=None, alias='group_by')
    highlight_full_fields: Optional[str] = Field(default=None, alias='highlight_full_fields')
    include_fields: Optional[str] = Field(default=None, alias='include_fields')
    max_facet_values: Optional[float] = Field(default=None, alias='max_facet_values')
    num_typos: Optional[float] = Field(default=None, alias='num_typos')
    page: Optional[float] = Field(default=None, alias='page')
    per_page: Optional[float] = Field(default=None, alias='per_page')
    prefix: Optional[str] = Field(default=None, alias='prefix')
    q: Optional[str] = Field(default=None, alias='q')
    query_by: Optional[str] = Field(default=None, alias='query_by')
    sort_by: Optional[str] = Field(default=None, alias='sort_by')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'SearchParameters[T]':
        """Create SearchParameters instance with typed data."""
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
