```python
from revenexx.client import Client
from revenexx.services.sites import Sites
from revenexx.models import Deployment
from revenexx.enums import SitesCreateTemplateDeploymentType

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

sites = Sites(client)

result: Deployment = sites.sites_create_vcs_deployment(
    site_id = '',
    reference = 'main',
    type = SitesCreateTemplateDeploymentType.BRANCH,
    activate = True # optional
)

print(result.model_dump())
```
