```python
from revenexx.client import Client
from revenexx.services.sites import Sites
from revenexx.models import VariableList

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

sites = Sites(client)

result: VariableList = sites.sites_list_variables(
    site_id = ''
)

print(result.model_dump())
```
