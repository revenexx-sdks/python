```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.apps import Apps
from revenexx_revenexx.models import Execution
from revenexx_revenexx.enums import Method

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

apps = Apps(client)

result: Execution = apps.apps_create_execution(
    function_id = '',
    async = None, # optional
    body = '', # optional
    headers = {}, # optional
    method = Method.GET, # optional
    path = '', # optional
    scheduled_at = '' # optional
)

print(result.model_dump())
```
