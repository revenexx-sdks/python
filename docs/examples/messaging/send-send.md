```python
from revenexx.client import Client
from revenexx.services.messaging import Messaging
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

messaging = Messaging(client)

result: Error = messaging.send_send(
    channel = '',
    template = '',
    to = '',
    attachments = [], # optional
    data = {}, # optional
    draft = True, # optional
    locale = '', # optional
    market = '', # optional
    send_at = '2026-01-01T12:00:00Z' # optional
)

print(result.model_dump())
```
