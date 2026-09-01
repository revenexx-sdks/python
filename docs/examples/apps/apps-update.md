```python
from revenexx.client import Client
from revenexx.services.apps import Apps
from revenexx.models import Function
from revenexx.enums import Runtime
from revenexx.enums import Scopes

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

apps = Apps(client)

result: Function = apps.apps_update(
    function_id = '',
    name = '',
    commands = 'npm install', # optional
    enabled = True, # optional
    entrypoint = 'src/main.js', # optional
    events = [], # optional
    execute = ["any"], # optional
    installation_id = '', # optional
    logging = True, # optional
    provider_branch = 'main', # optional
    provider_repository_id = '', # optional
    provider_root_directory = '', # optional
    provider_silent_mode = True, # optional
    runtime = Runtime.NODE_18_0, # optional
    schedule = '0 3 * * *', # optional
    scopes = [Scopes.SESSIONS_WRITE], # optional
    specification = 's-1vcpu-512mb', # optional
    timeout = 1 # optional
)

print(result.model_dump())
```
