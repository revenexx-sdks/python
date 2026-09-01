from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .facet_count import FacetCount
from .search_hit import SearchHit

T = TypeVar('T')

class SearchResult(AppwriteModel, Generic[T]):
    """
    A Typesense search response, passed through verbatim.

    Attributes
    ----------
    facet_counts : Optional[List[FacetCount[T]]]
        Typed model field.
    found : Optional[float]
        Total matching documents.
    hits : Optional[List[SearchHit[T]]]
        Typed model field.
    out_of : Optional[float]
        Documents searched.
    page : Optional[float]
        1-based page this result is for.
    search_time_ms : Optional[float]
        Typed model field.
    """
    facet_counts: Optional[List[FacetCount[T]]] = Field(default=None, alias='facet_counts')
    found: Optional[float] = Field(default=None, alias='found')
    hits: Optional[List[SearchHit[T]]] = Field(default=None, alias='hits')
    out_of: Optional[float] = Field(default=None, alias='out_of')
    page: Optional[float] = Field(default=None, alias='page')
    search_time_ms: Optional[float] = Field(default=None, alias='search_time_ms')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'SearchResult[T]':
        """Create SearchResult instance with typed data."""
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
