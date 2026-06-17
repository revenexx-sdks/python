```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.sites import Sites
from revenexx_revenexx.models import Deployment
from revenexx_revenexx.enums import Type

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

sites = Sites(client)

result: Deployment = sites.sites_create_template_deployment(
    site_id = '',
    owner = '',
    reference = '',
    repository = '',
    root_directory = '',
    type = Type.BRANCH,
    activate = None # optional
)

print(result.model_dump())
```
