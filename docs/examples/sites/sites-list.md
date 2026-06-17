```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.sites import Sites
from revenexx_revenexx.models import SiteList

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

sites = Sites(client)

result: SiteList = sites.sites_list(
    queries = [], # optional
    search = '', # optional
    total = None # optional
)

print(result.model_dump())
```
