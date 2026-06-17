```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.apps import Apps
from revenexx_revenexx.models import FunctionList

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

apps = Apps(client)

result: FunctionList = apps.apps_list(
    queries = [], # optional
    search = '', # optional
    total = None # optional
)

print(result.model_dump())
```
