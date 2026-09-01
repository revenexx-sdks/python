```python
from revenexx.client import Client
from revenexx.services.apps import Apps
from revenexx.models import TemplateFunctionList
from revenexx.enums import Runtimes
from revenexx.enums import UseCases

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

apps = Apps(client)

result: TemplateFunctionList = apps.apps_list_templates(
    runtimes = [Runtimes.NODE_18_0], # optional
    use_cases = [UseCases.STARTER], # optional
    limit = 1, # optional
    offset = 1, # optional
    total = True # optional
)

print(result.model_dump())
```
