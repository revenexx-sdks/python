from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .cart_abandon_sweep import CartAbandonSweep
from .cart_purge_sweep import CartPurgeSweep

class CartMaintenanceResult(AppwriteModel):
    """
    

    Attributes
    ----------
    abandon : Optional[CartAbandonSweep]
        The first sweep: active carts nobody has touched since their market&#039;s window become abandoned. Nothing else in the platform ever stamps abandoned_at, so without this the abandonment funnel is empty by construction rather than empty because nobody abandons carts.
    dry_run : Optional[bool]
        This pass wrote nothing. The counts and cart ids are the same ones the wet run would produce.
    purge : Optional[CartPurgeSweep]
        The second sweep, and the only destructive thing this app does: carts past their retention window are deleted, their lines with them. An ordered cart is never touched at any setting — it is the source record of a sale.
    swept_at : Optional[str]
        The instant this pass measured every window against. One clock for both sweeps, so a cart cannot be judged idle by one and fresh by the other.
    """
    abandon: Optional[CartAbandonSweep] = Field(default=None, alias='abandon')
    dry_run: Optional[bool] = Field(default=None, alias='dry_run')
    purge: Optional[CartPurgeSweep] = Field(default=None, alias='purge')
    swept_at: Optional[str] = Field(default=None, alias='swept_at')
