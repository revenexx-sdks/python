```python
from revenexx.client import Client
from revenexx.services.sites import Sites
from revenexx.models import Deployment
from revenexx.enums import SitesCreateTemplateDeploymentType

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
    type = SitesCreateTemplateDeploymentType.BRANCH,
    activate = True # optional
)

print(result.model_dump())
```
