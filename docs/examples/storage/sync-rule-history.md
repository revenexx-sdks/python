```python
from revenexx.client import Client
from revenexx.services.storage import Storage

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

storage = Storage(client)

result = storage.sync_rule_history(
    rule_id = '', # optional
    from = '2026-01-01T12:00:00Z', # optional
    to = '2026-01-01T12:00:00Z' # optional
)
```
