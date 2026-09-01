```python
from revenexx.client import Client
from revenexx.services.payments_ledger import PaymentsLedger
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

payments_ledger = PaymentsLedger(client)

result: Error = payments_ledger.payments_create(
    amount = 49.9,
    method_code = 'invoice',
    cart_id = '', # optional
    contact_id = '', # optional
    country = 'DE', # optional
    currency = 'EUR', # optional
    idempotency_key = 'checkout-2f9c41', # optional
    metadata = {
        "order_source": "web"
    }, # optional
    order_ref = 'ORD-10042', # optional
    return_url = 'https://shop.example.com/checkout/return' # optional
)

print(result.model_dump())
```
