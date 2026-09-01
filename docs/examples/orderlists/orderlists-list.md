```python
from revenexx.client import Client
from revenexx.services.orderlists import Orderlists
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orderlists = Orderlists(client)

result: Error = orderlists.orderlists_list(
    owner_id = '', # optional
    organization_id = '', # optional
    kind = 'shopping', # optional
    limit = 50, # optional
    offset = 0, # optional
    order = 'created_at.desc' # optional
)

print(result.model_dump())
```
