```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.messaging import Messaging

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

messaging = Messaging(client)

result = messaging.messaging_delete(
    message_id = ''
)
```
