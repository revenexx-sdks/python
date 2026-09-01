```python
from revenexx.client import Client
from revenexx.services.events import Events

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

events = Events(client)

result = events.events_get_catalog(
    fields = 'topic,channel' # optional
)
```
