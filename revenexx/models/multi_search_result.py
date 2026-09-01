from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .search_result import SearchResult

T = TypeVar('T')

class MultiSearchResult(AppwriteModel, Generic[T]):
    """
    

    Attributes
    ----------
    results : List[SearchResult[T]]
        One result per entry in `searches`, in the same order.
    """
    results: List[SearchResult[T]] = Field(..., alias='results')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'MultiSearchResult[T]':
        """Create MultiSearchResult instance with typed data."""
        instance = cls.model_validate(data)
        if 'results' in data and data['results'] is not None:
            instance.results = [
                SearchResult.with_data(row, model_type) 
                for row in data['results']
            ]
        return instance
