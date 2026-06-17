```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.payments import Payments
from revenexx_revenexx.models import PaymentProvider

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

payments = Payments(client)

result: PaymentProvider = payments.payments_providers_create(
    provider = '',
    credentials = {}, # optional
    enabled = None, # optional
    name = '', # optional
    options = {}, # optional
    test_mode = None, # optional
    webhook_secret = '' # optional
)

print(result.model_dump())
```
