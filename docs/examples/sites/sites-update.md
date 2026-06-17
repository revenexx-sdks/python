```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.sites import Sites
from revenexx_revenexx.models import Site
from revenexx_revenexx.enums import Framework
from revenexx_revenexx.enums import Adapter
from revenexx_revenexx.enums import BuildRuntime

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

sites = Sites(client)

result: Site = sites.sites_update(
    site_id = '',
    framework = Framework.ANALOG,
    name = '',
    adapter = Adapter.STATIC, # optional
    build_command = '', # optional
    build_runtime = BuildRuntime.NODE_18_0, # optional
    enabled = None, # optional
    fallback_file = '', # optional
    install_command = '', # optional
    installation_id = '', # optional
    logging = None, # optional
    output_directory = '', # optional
    provider_branch = '', # optional
    provider_repository_id = '', # optional
    provider_root_directory = '', # optional
    provider_silent_mode = None, # optional
    specification = '', # optional
    timeout = None # optional
)

print(result.model_dump())
```
