from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PaymentProviderUpdateRequest(AppwriteModel):
    """
    Partial update — omitted fields keep their current value.

    Attributes
    ----------
    credentials : Optional[Dict[str, Any]]
        The PSP&#039;s own API credentials, under the key names its auth scheme expects — `GET /payments/providers/catalog` publishes them per provider as `credential_fields` (Stripe: `api_key`; PayPal: `client_id` + `client_secret`; Novalnet: `api_key` + `payment_access_key` + `tariff_id`). They come from the provider&#039;s own dashboard, are handed to the driver in-process, and are never read back by any route. Write-only: to rotate one, write the new value. Whatever a document shows here is a placeholder.
    enabled : Optional[bool]
        Only an enabled provider takes NEW payments: a method pointing at a disabled one falls through to the tenant&#039;s `fallback_provider`, and to a 422 if there is none. Nothing else reads it — capture, cancel and refund on the payments this PSP already holds go on working — which is what makes disabling the safe retirement and deleting the refused one. Defaults to false — finish the credentials before switching it on.
    name : Optional[str]
        Operator-facing name of the configuration. Defaults to the catalog label, and is worth changing when a tenant runs two accounts with one PSP. Written straight to the database, which refuses an empty one.
    options : Optional[Dict[str, Any]]
        Per-provider switches this app understands, plus anything the merchant keeps beside them. Three keys are the app&#039;s own: `logo_url` (the bundled logo, filled in when the provider is seeded), `capture_method` and `three_ds` (what the prism driver does today). Free jsonb — an unknown key is stored and ignored.
    provider : Optional[str]
        The catalog code of the PSP this row configures — one row per provider per tenant. GET /payments/providers/catalog lists every code that may appear here. It is what every payment and every method naming this PSP resolves it by, so changing it is refused with 409 for as long as one of them does. Required on create, and refused with 400 when the catalog does not carry it.
    test_mode : Optional[bool]
        Whether the driver talks to the PSP&#039;s sandbox. New configurations start in test mode: a provider nobody verified must not touch live money. Unstated takes the tenant&#039;s own `test_mode_default` setting.
    webhook_secret : Optional[str]
        The signing secret the PSP issues when its webhook endpoint is created, in the provider&#039;s own dashboard. webhooks.revenexx.com verifies each callback against it before the dispatcher hands the envelope to this app. Write-only, like `credentials`: it is stored, used, and never read back by any route, so there is nothing to compare a value against — to rotate it, write the new one. Whatever a document shows here is a generated placeholder, not a usable secret — writing it verbatim leaves every callback failing verification.
    """
    credentials: Optional[Dict[str, Any]] = Field(default=None, alias='credentials')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    name: Optional[str] = Field(default=None, alias='name')
    options: Optional[Dict[str, Any]] = Field(default=None, alias='options')
    provider: Optional[str] = Field(default=None, alias='provider')
    test_mode: Optional[bool] = Field(default=None, alias='test_mode')
    webhook_secret: Optional[str] = Field(default=None, alias='webhook_secret')
