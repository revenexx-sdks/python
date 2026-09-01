from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.payment_dunning_stage import PaymentDunningStage
from ..enums.payment_failure_code import PaymentFailureCode
from ..enums.payment_method_kind import PaymentMethodKind
from ..enums.payment_status import PaymentStatus

class Payment(AppwriteModel):
    """
    

    Attributes
    ----------
    amount : Optional[float]
        What the provider is asked to authorize, in `currency`. 0 is legal (a free order) and negative is refused by the handler and by the CHECK behind it. `fee_amount` is recorded beside this and is NOT added to it — a checkout that charges its payment surcharge sends a total that already includes it.
    authorized_at : Optional[str]
        When the money was reserved — or, for invoice and prepayment, when it became owed. The clock the capture window and the dunning stages are measured from.
    captured_at : Optional[str]
        When the money was actually taken. The refund window is measured from here.
    cart_id : Optional[str]
        The cart this payment pays for. Not a foreign key: the payment is a record of what happened and outlives the cart. Indexed, so it is the cheap way to find the payment behind a checkout.
    contact_id : Optional[str]
        The paying customer contact. Not a foreign key — a payment must survive a contact being merged or erased. Indexed.
    created_at : Optional[str]
        When the payment was created. The dunning clock for invoice and prepayment runs from here.
    currency : Optional[str]
        ISO 4217 code the amount and the fee are in. The database bounds the length at three characters and nothing else, so lower case is stored as written.
    dunning_due_at : Optional[str]
        When the NEXT dunning stage falls due — the moment a reminder becomes due, then the moment it becomes overdue. null once nothing further is pending, which includes an already overdue payment and every paid, cancelled or refunded one.
    dunning_stage : Optional[PaymentDunningStage]
        How overdue an unpaid self-managed payment is: &#039;none&#039;, &#039;reminder&#039; or &#039;overdue&#039;. Written by the daily dunning scan from the merchant&#039;s two thresholds, and reset the moment the money arrives or the claim is dropped. It classifies and never sends: what a reminder looks like is the merchant&#039;s own workflow.
    error_code : Optional[PaymentFailureCode]
        The class of failure, out of a fixed taxonomy — the value to branch on. null unless the payment failed. The five classes say what a caller can DO: &#039;provider_unavailable&#039;, &#039;provider_unreachable&#039;, &#039;provider_not_configured&#039;, &#039;provider_declined&#039;, &#039;provider_error&#039; — a provider that is unreachable or unavailable is worth a retry, a declined payment needs a different method from the buyer, and a provider that is not configured needs an operator.
    error_message : Optional[str]
        One operator-facing sentence, fixed per `error_code`. Never the provider&#039;s or the runtime&#039;s own wording: that is unbounded internal text and it stays in the app log.
    failed_at : Optional[str]
        When the payment failed. `error_code` says which class of failure.
    fee_amount : Optional[float]
        The method surcharge as it was computed at creation, in `currency`. Kept so the fee that was quoted stays readable after the method&#039;s fee configuration changes.
    id : Optional[str]
        Id of the payment. Every lifecycle route addresses it, and it is what the drivers send the provider as their merchant transaction reference.
    idempotency_key : Optional[str]
        The caller&#039;s own key for this creation attempt. Sending it again answers the SAME payment with 200 instead of creating a second one — which is what makes a retried checkout safe. Unique per tenant, so a filter on it answers at most one row.
    kind : Optional[PaymentMethodKind]
        Copied from the method at creation. &#039;self_managed&#039; payments move through the lifecycle without a PSP; &#039;psp&#039; payments are driven by `provider`.
    metadata : Optional[Dict[str, Any]]
        Whatever the creating call sent, plus the keys this app writes onto it. The app&#039;s own: `provider_method` (the method&#039;s provider-side id, copied at creation), `return_url` (where the PSP sends the buyer back), `cancel_reason` / `refund_reason` (the operator&#039;s words from the cancel and refund routes, also handed to the provider) and `provider_fallback_from` (the provider that was WANTED, written when the tenant&#039;s fallback_provider stood in — the only record of why the money went through a different acquirer). Free jsonb; a caller&#039;s own keys are kept untouched beside these.
    method_code : Optional[str]
        The `code` of the payment method this payment was made with, copied at creation. Deliberately a code and not a foreign key: the ledger records what happened and has to outlive the configuration it happened under.
    next_action : Optional[Dict[str, Any]]
        What the storefront must do before this payment can go any further, or null when there is nothing to do. It is set exactly when `status` is `requires_action`, and every transition clears it. One shape exists today: `{ &quot;type&quot;: &quot;redirect&quot;, &quot;url&quot;: … }` — send the buyer to `url` (that is also where a 3-D Secure challenge is presented, because the connector hands it back as a redirect), and when they come back call POST /payments/{id}/confirm. `type` is what to branch on; a client that does not recognise it must not guess.
    order_ref : Optional[str]
        The external order reference the checkout wrote onto the payment. It is what POST /payments/orders/{order_ref}/capture resolves and the fallback key a PSP webhook is matched on when it carries no transaction id — so an integration that leaves it null gives up both. Free text with no uniqueness: several payments may share one reference.
    provider : Optional[str]
        The PSP the money really went through — resolved at creation and rewritten if the tenant&#039;s fallback provider stood in, in which case `metadata.provider_fallback_from` records what was meant. null for self-managed payments.
    psp_payment_id : Optional[str]
        The provider&#039;s own transaction id, as it answered — the value to quote in a PSP support case, and the primary key a webhook is matched on. Shaped by the provider, so nothing here constrains it; null until a provider has answered, and always null for self-managed payments.
    refunded_at : Optional[str]
        When the payment was refunded in full — this app has no partial refund to record.
    status : Optional[PaymentStatus]
        Where the payment stands. &#039;created&#039; → &#039;requires_action&#039; → &#039;authorized&#039; → &#039;captured&#039; → &#039;refunded&#039;, with &#039;failed&#039; and &#039;cancelled&#039; ending it. GET /payments/vocabularies/statuses serves the same set with labels, badge tones and which of them are final.
    tenant_id : Optional[str]
        The tenant the row belongs to — the same slug the request carried in `X-Revenexx-Tenant`. Added by the platform rather than by this app, and echoed so a caller that fans several tenants into one store can tell the rows apart.
    updated_at : Optional[str]
        When the row last moved. For a PSP payment still waiting on a callback this is what the webhook-staleness check measures against, so an old payment that changed a minute ago counts as progressing.
    """
    amount: Optional[float] = Field(default=None, alias='amount')
    authorized_at: Optional[str] = Field(default=None, alias='authorized_at')
    captured_at: Optional[str] = Field(default=None, alias='captured_at')
    cart_id: Optional[str] = Field(default=None, alias='cart_id')
    contact_id: Optional[str] = Field(default=None, alias='contact_id')
    created_at: Optional[str] = Field(default=None, alias='created_at')
    currency: Optional[str] = Field(default=None, alias='currency')
    dunning_due_at: Optional[str] = Field(default=None, alias='dunning_due_at')
    dunning_stage: Optional[PaymentDunningStage] = Field(default=None, alias='dunning_stage')
    error_code: Optional[PaymentFailureCode] = Field(default=None, alias='error_code')
    error_message: Optional[str] = Field(default=None, alias='error_message')
    failed_at: Optional[str] = Field(default=None, alias='failed_at')
    fee_amount: Optional[float] = Field(default=None, alias='fee_amount')
    id: Optional[str] = Field(default=None, alias='id')
    idempotency_key: Optional[str] = Field(default=None, alias='idempotency_key')
    kind: Optional[PaymentMethodKind] = Field(default=None, alias='kind')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
    method_code: Optional[str] = Field(default=None, alias='method_code')
    next_action: Optional[Dict[str, Any]] = Field(default=None, alias='next_action')
    order_ref: Optional[str] = Field(default=None, alias='order_ref')
    provider: Optional[str] = Field(default=None, alias='provider')
    psp_payment_id: Optional[str] = Field(default=None, alias='psp_payment_id')
    refunded_at: Optional[str] = Field(default=None, alias='refunded_at')
    status: Optional[PaymentStatus] = Field(default=None, alias='status')
    tenant_id: Optional[str] = Field(default=None, alias='tenant_id')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
