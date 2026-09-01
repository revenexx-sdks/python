```python
from revenexx.client import Client
from revenexx.services.payments_providers import PaymentsProviders

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

payments_providers = PaymentsProviders(client)

result = payments_providers.payments_providers_catalog()
```
