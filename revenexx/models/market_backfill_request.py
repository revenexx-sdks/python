from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MarketBackfillRequest(AppwriteModel):
    """
    The path id is the market being REPAIRED; `source` is the market to copy from (a uuid or a market code). The three flags default to true.

    Attributes
    ----------
    currencies : Optional[bool]
        Take the source&#039;s traded currencies for codes this market does not already carry. Default true.
    locales : Optional[bool]
        Take the source&#039;s locales for codes this market does not already carry. Default true.
    source : str
        The market to copy the missing pieces FROM — a uuid or a market code. Must not be the market in the path. Pick a market that is already right; nothing about it is changed.
    tax_classes : Optional[bool]
        Take the source&#039;s tax classes for codes this market does not already carry. An existing code keeps ITS rate — a backfill never re-rates a class the merchant already set. Default true.
    """
    currencies: Optional[bool] = Field(default=None, alias='currencies')
    locales: Optional[bool] = Field(default=None, alias='locales')
    source: str = Field(..., alias='source')
    tax_classes: Optional[bool] = Field(default=None, alias='tax_classes')
