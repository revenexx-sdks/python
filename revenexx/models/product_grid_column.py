from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.product_grid_column_source import ProductGridColumnSource

class ProductGridColumn(AppwriteModel):
    """
    

    Attributes
    ----------
    code : Optional[str]
        The key to read out of a row: a column name for the fixed columns, an attribute code for the rest (then it is a key of the row&#039;s `attributes` object).
    label : Optional[Dict[str, Any]]
        The attribute&#039;s i18n labels, or a plain title for the fixed columns.
    source : Optional[ProductGridColumnSource]
        Where the value comes from: &#039;column&#039; is a plain products column, &#039;attribute&#039; a key inside `attribute_values`, &#039;resolved&#039; something this route computed (the display name).
    type : Optional[str]
        Which control renders the cell — the same widget vocabulary `GET /products/attribute-schema` uses, so one renderer serves both.
    """
    code: Optional[str] = Field(default=None, alias='code')
    label: Optional[Dict[str, Any]] = Field(default=None, alias='label')
    source: Optional[ProductGridColumnSource] = Field(default=None, alias='source')
    type: Optional[str] = Field(default=None, alias='type')
