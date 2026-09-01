```python
from revenexx.client import Client
from revenexx.services.search import Search

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

search = Search(client)

result = search.gateway_facet_resync(
    app = '', # optional
    vendor = '' # optional
)
```
