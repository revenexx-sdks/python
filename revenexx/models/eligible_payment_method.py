from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.payment_fee_type import PaymentFeeType
from ..enums.payment_method_kind import PaymentMethodKind

class EligiblePaymentMethod(AppwriteModel):
    """
    One method as a checkout should render it: identity, wording, and what it costs this buyer.

    Attributes
    ----------
    code : Optional[str]
        The code to send back as `method_code` when the payment is created.
    currency : Optional[str]
        The currency `fee` is in — the one the request asked with, echoed.
    description : Optional[str]
        The merchant&#039;s line about this method, to show beside it at checkout.
    fee : Optional[float]
        The surcharge this method costs THIS buyer, already computed against the requested amount — a fixed fee as it stands, a percentage resolved into an amount. Not a column: no CHECK bounds it, so none is declared.
    fee_type : Optional[PaymentFeeType]
        How `fee` was arrived at, for a checkout that wants to show &quot;2 % surcharge&quot; rather than the amount.
    kind : Optional[PaymentMethodKind]
        Whether choosing this method starts a PSP flow (&#039;psp&#039;) or authorizes immediately (&#039;self_managed&#039;).
    labels : Optional[Dict[str, Any]]
        Buyer-facing names keyed by language tag, or null when the merchant configured none — then `name` is all there is.
    name : Optional[str]
        The operator-facing name. Prefer `labels` for anything a buyer reads.
    position : Optional[float]
        The merchant&#039;s sort order. The list is already sorted by it; it is carried so a client that re-sorts can put it back.
    provider : Optional[str]
        The PSP behind it, for a checkout that has to load a provider SDK before it can collect an instrument. null for self-managed methods.
    """
    code: Optional[str] = Field(default=None, alias='code')
    currency: Optional[str] = Field(default=None, alias='currency')
    description: Optional[str] = Field(default=None, alias='description')
    fee: Optional[float] = Field(default=None, alias='fee')
    fee_type: Optional[PaymentFeeType] = Field(default=None, alias='fee_type')
    kind: Optional[PaymentMethodKind] = Field(default=None, alias='kind')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    provider: Optional[str] = Field(default=None, alias='provider')
