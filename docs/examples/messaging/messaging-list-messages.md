```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.messaging import Messaging
from revenexx_revenexx.models import MessageList

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

messaging = Messaging(client)

result: MessageList = messaging.messaging_list_messages(
    queries = [], # optional
    search = '', # optional
    total = None # optional
)

print(result.model_dump())
```
