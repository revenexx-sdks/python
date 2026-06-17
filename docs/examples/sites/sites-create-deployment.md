```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.sites import Sites
from revenexx_revenexx.models import Deployment

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

sites = Sites(client)

result: Deployment = sites.sites_create_deployment(
    site_id = '',
    activate = None,
    code = '',
    build_command = '', # optional
    install_command = '', # optional
    output_directory = '' # optional
)

print(result.model_dump())
```
