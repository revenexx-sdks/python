```python
from revenexx.client import Client
from revenexx.services.apps import Apps
from revenexx.models import Deployment

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

apps = Apps(client)

result: Deployment = apps.apps_create_duplicate_deployment(
    function_id = '',
    deployment_id = '',
    build_id = '' # optional
)

print(result.model_dump())
```
