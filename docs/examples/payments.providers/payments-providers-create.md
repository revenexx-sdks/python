```python
from revenexx.client import Client
from revenexx.services.payments_providers import PaymentsProviders
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

payments_providers = PaymentsProviders(client)

result: Error = payments_providers.payments_providers_create(
    provider = 'stripe',
    credentials = {}, # optional
    enabled = True, # optional
    name = 'Stripe', # optional
    options = {
        "capture_method": "automatic",
        "logo_url": "https:\/\/apps.example.com\/payments\/logos\/stripe",
        "three_ds": False
    }, # optional
    test_mode = True, # optional
    webhook_secret = '' # optional
)

print(result.model_dump())
```
