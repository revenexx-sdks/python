from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.payment_fee_type import PaymentFeeType
from ..enums.payment_method_kind import PaymentMethodKind

class PaymentMethodCreateRequest(AppwriteModel):
    """
    A method needs its identity: code + name.

    Attributes
    ----------
    code : str
        Stable method code (unique per tenant, e.g. &#039;invoice&#039;, &#039;card&#039;).
    countries : Optional[List[Any]]
        Allowed ISO country codes — empty/omitted = unrestricted.
    description : Optional[str]
        Typed model field.
    enabled : Optional[bool]
        Disabled methods are never eligible (default false).
    fee_amount : Optional[float]
        Fixed amount or percent value, per fee_type (default 0).
    fee_currency : Optional[str]
        ISO 4217 code (default EUR).
    fee_type : Optional[PaymentFeeType]
        How &#039;fee_amount&#039; applies (default &#039;none&#039;).
    kind : Optional[PaymentMethodKind]
        Self-managed (merchant fulfils, default) or PSP-backed (&#039;provider&#039; required to transact).
    labels : Optional[Dict[str, Any]]
        Localized display names ({ de, en, … }).
    max_order_value : Optional[float]
        Maximum order amount — omitted = no upper bound.
    metadata : Optional[Dict[str, Any]]
        Free-form metadata.
    min_order_value : Optional[float]
        Minimum order amount — omitted = no lower bound.
    name : str
        Display name.
    position : Optional[float]
        Sort position in the checkout (default 0).
    provider : Optional[str]
        PSP code from the catalog — only for kind &#039;psp&#039;.
    provider_method : Optional[str]
        The provider&#039;s payment method id (e.g. &#039;card&#039;, &#039;paypal&#039;).
    """
    code: str = Field(..., alias='code')
    countries: Optional[List[Any]] = Field(default=None, alias='countries')
    description: Optional[str] = Field(default=None, alias='description')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    fee_amount: Optional[float] = Field(default=None, alias='fee_amount')
    fee_currency: Optional[str] = Field(default=None, alias='fee_currency')
    fee_type: Optional[PaymentFeeType] = Field(default=None, alias='fee_type')
    kind: Optional[PaymentMethodKind] = Field(default=None, alias='kind')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    max_order_value: Optional[float] = Field(default=None, alias='max_order_value')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    min_order_value: Optional[float] = Field(default=None, alias='min_order_value')
    name: str = Field(..., alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    provider: Optional[str] = Field(default=None, alias='provider')
    provider_method: Optional[str] = Field(default=None, alias='provider_method')
