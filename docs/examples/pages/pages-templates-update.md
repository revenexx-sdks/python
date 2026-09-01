```python
from revenexx.client import Client
from revenexx.services.pages import Pages
from revenexx.models import Error
from revenexx.models import PageBlockTree

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages = Pages(client)

result: Error = pages.pages_templates_update(
    id = '',
    description = 'Full-width hero followed by a two-column teaser row.', # optional
    field_name = 'content', # optional
    is_default = True, # optional
    label = 'Hero with two teasers', # optional
    page_bundle = 'standard', # optional
    tree = [PageBlockTree()] # optional
)

print(result.model_dump())
```
