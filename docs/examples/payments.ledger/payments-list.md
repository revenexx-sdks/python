```python
from revenexx.client import Client
from revenexx.services.payments_ledger import PaymentsLedger
from revenexx.enums import PaymentStatus
from revenexx.enums import PaymentMethodKind
from revenexx.enums import PaymentDunningStage

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

payments_ledger = PaymentsLedger(client)

result = payments_ledger.payments_list(
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc', # optional
    cart_id = '', # optional
    contact_id = '', # optional
    status = PaymentStatus.CREATED, # optional
    order_ref = 'ORD-10042', # optional
    method_code = 'invoice', # optional
    kind = PaymentMethodKind.SELF_MANAGED, # optional
    provider = 'stripe', # optional
    dunning_stage = PaymentDunningStage.NONE, # optional
    idempotency_key = 'checkout-2f9c41' # optional
)
```
