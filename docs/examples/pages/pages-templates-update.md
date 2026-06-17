```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.pages import Pages
from revenexx_revenexx.models import Template

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages = Pages(client)

result: Template = pages.pages_templates_update(
    id = '',
    description = '', # optional
    field_name = '', # optional
    is_default = None, # optional
    label = '', # optional
    page_bundle = '', # optional
    tree = [] # optional
)

print(result.model_dump())
```
