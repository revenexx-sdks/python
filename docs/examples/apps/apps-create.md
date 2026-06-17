```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.apps import Apps
from revenexx_revenexx.models import Function
from revenexx_revenexx.enums import Runtime
from revenexx_revenexx.enums import Scopes

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

apps = Apps(client)

result: Function = apps.apps_create(
    function_id = '',
    name = '',
    runtime = Runtime.NODE_18_0,
    commands = '', # optional
    enabled = None, # optional
    entrypoint = '', # optional
    events = [], # optional
    execute = [], # optional
    installation_id = '', # optional
    logging = None, # optional
    provider_branch = '', # optional
    provider_repository_id = '', # optional
    provider_root_directory = '', # optional
    provider_silent_mode = None, # optional
    schedule = '', # optional
    scopes = [Scopes.SESSIONS_WRITE], # optional
    specification = '', # optional
    timeout = None # optional
)

print(result.model_dump())
```
