```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.apps import Apps
from revenexx_revenexx.models import Deployment

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

apps = Apps(client)

result: Deployment = apps.apps_create_deployment(
    function_id = '',
    activate = None,
    code = '',
    commands = '', # optional
    entrypoint = '' # optional
)

print(result.model_dump())
```
