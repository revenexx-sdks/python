from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.payment_fee_type import PaymentFeeType
from ..enums.payment_method_kind import PaymentMethodKind

class PaymentMethod(AppwriteModel):
    """
    

    Attributes
    ----------
    code : Optional[str]
        The machine name of the method, unique per tenant and lower case by convention (&#039;invoice&#039;, &#039;prepayment&#039;, &#039;card&#039;, &#039;paypal&#039;). It is the string the checkout asks for, the string every payment stores, and therefore the one value here that cannot be changed freely: renaming it would leave the ledger naming something that no longer exists, so it is refused with 409 for as long as any payment names it.
    countries : Optional[List[Any]]
        Allowed ISO 3166-1 alpha-2 country codes, compared upper-cased against the buyer country. null or an empty list means unrestricted — the invoice method this app seeds is restricted to DE, which is why an eligibility call without a country sees it excluded.
    created_at : Optional[str]
        When this configuration was created.
    description : Optional[str]
        One line explaining the method where it is offered — payment terms, what happens after the order. Shown to the buyer, so it is the merchant&#039;s wording rather than the app&#039;s.
    enabled : Optional[bool]
        A disabled method is never eligible and never reaches a checkout. This is the switch an operator wants: deleting a method the ledger still names — or renaming its `code` — is refused with 409.
    fee_amount : Optional[float]
        The surcharge this method costs the buyer, read as an amount or as a percentage depending on `fee_type`. Never negative — a discount for paying a certain way is not expressible here.
    fee_currency : Optional[str]
        ISO 4217 code a fixed fee is expressed in. The database bounds the length at three characters and nothing else, so lower case is stored as written.
    fee_type : Optional[PaymentFeeType]
        How `fee_amount` applies: &#039;none&#039; (no surcharge), &#039;fixed&#039; (that many units of `fee_currency`) or &#039;percent&#039; (that share of the order amount).
    id : Optional[str]
        Id of the configuration row. A payment names its method by `code`, never by this — so an id is only ever used to address the configuration itself.
    kind : Optional[PaymentMethodKind]
        Who moves the money. &#039;self_managed&#039; — invoice, prepayment — means the merchant fulfils and reconciles it outside any PSP, and such a payment authorizes the moment it is created. &#039;psp&#039; means a configured provider authorizes, captures and refunds it.
    labels : Optional[Dict[str, Any]]
        Buyer-facing names keyed by language tag — what a storefront shows instead of the operator-facing `name`. Free jsonb: the database constrains neither the tags nor the values, so a client reads the tag it wants and falls back to `en`.
    max_order_value : Optional[float]
        Largest order amount this method may be used for — the usual credit-risk cap on invoice and prepayment. null means no upper bound.
    metadata : Optional[Dict[str, Any]]
        Free-form merchant data carried on the configuration. This app never reads it — it is storage for the integrations that do (an ERP key for the method, a ledger account, a display hint).
    min_order_value : Optional[float]
        Smallest order amount this method may be used for — the usual guard against paying a €5 order by invoice. null means no lower bound.
    name : Optional[str]
        Operator-facing name, in the language the merchant administers in. What a buyer sees comes from `labels`.
    position : Optional[float]
        Sort order at checkout, ascending — the merchant&#039;s preferred payment method first.
    provider : Optional[str]
        The PSP code this method transacts through, from GET /payments/providers/catalog. Only meaningful for kind &#039;psp&#039;; a PSP method that names none falls back to the tenant&#039;s `default_provider` setting.
    provider_method : Optional[str]
        The provider&#039;s own payment-method id (&#039;card&#039;, &#039;paypal&#039;, &#039;sepa_debit&#039;) — what the driver is told to charge. Copied onto every payment created with this method as `metadata.provider_method`.
    tenant_id : Optional[str]
        The tenant the row belongs to — the same slug the request carried in `X-Revenexx-Tenant`. Added by the platform rather than by this app, and echoed so a caller that fans several tenants into one store can tell the rows apart.
    updated_at : Optional[str]
        When it was last changed. The eligibility answer is computed live, so this is the age of the configuration and not of any cached result.
    """
    code: Optional[str] = Field(default=None, alias='code')
    countries: Optional[List[Any]] = Field(default=None, alias='countries')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    description: Optional[str] = Field(default=None, alias='description')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    fee_amount: Optional[float] = Field(default=None, alias='fee_amount')
    fee_currency: Optional[str] = Field(default=None, alias='fee_currency')
    fee_type: Optional[PaymentFeeType] = Field(default=None, alias='fee_type')
    id: Optional[str] = Field(default=None, alias='id')
    kind: Optional[PaymentMethodKind] = Field(default=None, alias='kind')
    labels: Optional[Dict[str, Any]] = Field(default=None, alias='labels')
    max_order_value: Optional[float] = Field(default=None, alias='max_order_value')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    min_order_value: Optional[float] = Field(default=None, alias='min_order_value')
    name: Optional[str] = Field(default=None, alias='name')
    position: Optional[float] = Field(default=None, alias='position')
    provider: Optional[str] = Field(default=None, alias='provider')
    provider_method: Optional[str] = Field(default=None, alias='provider_method')
    tenant_id: Optional[str] = Field(default=None, alias='tenant_id')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
