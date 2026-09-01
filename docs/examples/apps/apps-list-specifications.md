```python
from revenexx.client import Client
from revenexx.services.apps import Apps
from revenexx.models import SpecificationList

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

apps = Apps(client)

result: SpecificationList = apps.apps_list_specifications()

print(result.model_dump())
```
