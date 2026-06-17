```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.apps import Apps
from revenexx_revenexx.models import TemplateFunctionList
from revenexx_revenexx.enums import Runtimes
from revenexx_revenexx.enums import UseCases

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

apps = Apps(client)

result: TemplateFunctionList = apps.apps_list_templates(
    runtimes = [Runtimes.NODE_18_0], # optional
    use_cases = [UseCases.STARTER], # optional
    limit = None, # optional
    offset = None, # optional
    total = None # optional
)

print(result.model_dump())
```
