```python
from revenexx.client import Client
from revenexx.services.orderlists import Orderlists
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orderlists = Orderlists(client)

result: Error = orderlists.orderlists_update(
    id = '',
    kind = 'shopping', # optional
    metadata = {
        "department": "facility",
        "erp_reference": "REQ-2026-0042"
    }, # optional
    name = 'Weekly office supplies', # optional
    shared = True # optional
)

print(result.model_dump())
```
