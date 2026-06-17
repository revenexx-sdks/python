```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.apps import Apps

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

apps = Apps(client)

result = apps.apps_delete_execution(
    function_id = '',
    execution_id = ''
)
```
