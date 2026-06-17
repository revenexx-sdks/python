```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.storage import Storage

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

storage = Storage(client)

result = storage.sync_rule_run_protocol(
    id = '',
    run_id = ''
)
```
