```python
from revenexx.client import Client
from revenexx.services.sites import Sites

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

sites = Sites(client)

result = sites.sites_delete_variable(
    site_id = '',
    variable_id = ''
)
```
