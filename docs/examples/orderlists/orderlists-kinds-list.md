```python
from revenexx.client import Client
from revenexx.services.orderlists import Orderlists

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orderlists = Orderlists(client)

result = orderlists.orderlists_kinds_list(
    limit = 50, # optional
    offset = 0 # optional
)
```
