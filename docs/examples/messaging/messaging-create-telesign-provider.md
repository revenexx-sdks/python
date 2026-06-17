```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.messaging import Messaging
from revenexx_revenexx.models import Provider

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

messaging = Messaging(client)

result: Provider = messaging.messaging_create_telesign_provider(
    name = '',
    provider_id = '',
    api_key = '', # optional
    customer_id = '', # optional
    enabled = None, # optional
    from = '' # optional
)

print(result.model_dump())
```
