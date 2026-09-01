```python
from revenexx.client import Client
from revenexx.services.messaging import Messaging
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

messaging = Messaging(client)

result: Error = messaging.binding_store(
    channel = '',
    event_topic = '',
    recipient = '',
    template_key = '',
    enabled = True, # optional
    fallback_order = 1, # optional
    locale = '' # optional
)

print(result.model_dump())
```
