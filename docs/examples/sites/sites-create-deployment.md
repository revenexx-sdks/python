```python
from revenexx.client import Client
from revenexx.services.sites import Sites
from revenexx.input_file import InputFile
from revenexx.models import Deployment

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

sites = Sites(client)

result: Deployment = sites.sites_create_deployment(
    site_id = '',
    activate = True,
    code = InputFile.from_path('file.png'),
    build_command = '', # optional
    install_command = '', # optional
    output_directory = '' # optional
)

print(result.model_dump())
```
