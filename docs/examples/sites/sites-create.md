```python
from revenexx.client import Client
from revenexx.services.sites import Sites
from revenexx.models import Site
from revenexx.enums import BuildRuntime
from revenexx.enums import Framework
from revenexx.enums import Adapter

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

sites = Sites(client)

result: Site = sites.sites_create(
    build_runtime = BuildRuntime.NODE_18_0,
    framework = Framework.ANALOG,
    name = '',
    site_id = '',
    adapter = Adapter.STATIC, # optional
    build_command = 'npm run build', # optional
    enabled = True, # optional
    fallback_file = 'index.html', # optional
    install_command = 'npm install', # optional
    installation_id = '', # optional
    logging = True, # optional
    output_directory = '', # optional
    provider_branch = 'main', # optional
    provider_repository_id = '', # optional
    provider_root_directory = '', # optional
    provider_silent_mode = True, # optional
    specification = 's-1vcpu-512mb', # optional
    timeout = 1 # optional
)

print(result.model_dump())
```
