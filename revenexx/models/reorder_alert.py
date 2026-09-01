from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.reorder_point_source import ReorderPointSource

class ReorderAlert(AppwriteModel):
    """
    

    Attributes
    ----------
    available : Optional[float]
        on_hand − reserved: the figure compared against the reorder point. Alerting on AVAILABLE rather than on_hand is the point of this list — a shelf that looks full but is entirely sold is exactly the row a buyer must see.
    location_code : Optional[str]
        That location&#039;s code, resolved for the reader so no second call is needed. Null if the location row could not be read.
    location_enabled : Optional[bool]
        Whether that location is enabled. A DISABLED location still alerts — its stock is invisible to availability, but the goods are real and somebody has to decide. Null if the location row could not be read.
    location_id : Optional[str]
        The location holding it.
    on_hand : Optional[float]
        What is physically there right now, promised units included.
    product_id : Optional[str]
        The product this row tracks, null when it is tracked by SKU.
    reorder_point : Optional[float]
        The threshold that was applied to this row — its own, or the tenant default.
    reorder_point_source : Optional[ReorderPointSource]
        &#039;row&#039; — the stock row&#039;s own threshold. &#039;default&#039; — the reorder_point_default setting.
    reserved : Optional[float]
        How much of it is already promised to orders.
    shortfall : Optional[float]
        How far below the point this row has fallen. The list is sorted by it, worst first.
    sku : Optional[str]
        The article number this row tracks, null when it is tracked by product id.
    stock_level_id : Optional[str]
        The stock row that is low — the id to correct or receive against (POST /inventories/stock/{id}/adjust).
    """
    available: Optional[float] = Field(default=None, alias='available')
    location_code: Optional[str] = Field(default=None, alias='location_code')
    location_enabled: Optional[bool] = Field(default=None, alias='location_enabled')
    location_id: Optional[str] = Field(default=None, alias='location_id')
    on_hand: Optional[float] = Field(default=None, alias='on_hand')
    product_id: Optional[str] = Field(default=None, alias='product_id')
    reorder_point: Optional[float] = Field(default=None, alias='reorder_point')
    reorder_point_source: Optional[ReorderPointSource] = Field(default=None, alias='reorder_point_source')
    reserved: Optional[float] = Field(default=None, alias='reserved')
    shortfall: Optional[float] = Field(default=None, alias='shortfall')
    sku: Optional[str] = Field(default=None, alias='sku')
    stock_level_id: Optional[str] = Field(default=None, alias='stock_level_id')
