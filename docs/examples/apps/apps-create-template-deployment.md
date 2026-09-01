```python
from revenexx.client import Client
from revenexx.services.apps import Apps
from revenexx.models import Deployment
from revenexx.enums import Type

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

apps = Apps(client)

result: Deployment = apps.apps_create_template_deployment(
    function_id = '',
    owner = '',
    reference = '',
    repository = '',
    root_directory = '',
    type = Type.COMMIT,
    activate = True # optional
)

print(result.model_dump())
```
