```python
from revenexx.client import Client
from revenexx.services.sites import Sites
from revenexx.models import Variable

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

sites = Sites(client)

result: Variable = sites.sites_get_variable(
    site_id = '',
    variable_id = ''
)

print(result.model_dump())
```
