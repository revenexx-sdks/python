from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class PaymentProvider(AppwriteModel):
    """
    

    Attributes
    ----------
    created_at : Optional[str]
        When this PSP was configured for the tenant.
    enabled : Optional[bool]
        Only an enabled provider takes NEW payments: a method pointing at a disabled one falls through to the tenant&#039;s `fallback_provider`, and to a 422 if there is none. Nothing else reads it — capture, cancel and refund on the payments this PSP already holds go on working — which is what makes disabling the safe retirement and deleting the refused one.
    id : Optional[str]
        Id of the PSP configuration row — what the provider routes address. The provider itself is named by `provider`.
    name : Optional[str]
        Operator-facing name of the configuration. Defaults to the catalog label, and is worth changing when a tenant runs two accounts with one PSP.
    options : Optional[Dict[str, Any]]
        Per-provider switches this app understands, plus anything the merchant keeps beside them. Three keys are the app&#039;s own: `logo_url` (the bundled logo, filled in when the provider is seeded), `capture_method` and `three_ds` (what the prism driver does today). Free jsonb — an unknown key is stored and ignored.
    provider : Optional[str]
        The catalog code of the PSP this row configures — one row per provider per tenant. GET /payments/providers/catalog lists every code that may appear here. It is what every payment and every method naming this PSP resolves it by, so changing it is refused with 409 for as long as one of them does.
    test_mode : Optional[bool]
        Whether the driver talks to the PSP&#039;s sandbox. New configurations start in test mode: a provider nobody verified must not touch live money.
    updated_at : Optional[str]
        When its configuration last changed — including a credential rotation, which is otherwise invisible from the outside.
    """
    created_at: Optional[str] = Field(default=None, alias='created_at')
    enabled: Optional[bool] = Field(default=None, alias='enabled')
    id: Optional[str] = Field(default=None, alias='id')
    name: Optional[str] = Field(default=None, alias='name')
    options: Optional[Dict[str, Any]] = Field(default=None, alias='options')
    provider: Optional[str] = Field(default=None, alias='provider')
    test_mode: Optional[bool] = Field(default=None, alias='test_mode')
    updated_at: Optional[str] = Field(default=None, alias='updated_at')
