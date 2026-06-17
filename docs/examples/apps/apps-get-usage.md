```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.apps import Apps
from revenexx_revenexx.models import UsageFunction
from revenexx_revenexx.enums import Range

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

apps = Apps(client)

result: UsageFunction = apps.apps_get_usage(
    function_id = '',
    range = Range.24H # optional
)

print(result.model_dump())
```
