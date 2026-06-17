```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.apps import Apps
from revenexx_revenexx.models import Deployment
from revenexx_revenexx.enums import Type

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

apps = Apps(client)

result: Deployment = apps.apps_create_vcs_deployment(
    function_id = '',
    reference = '',
    type = Type.BRANCH,
    activate = None # optional
)

print(result.model_dump())
```
