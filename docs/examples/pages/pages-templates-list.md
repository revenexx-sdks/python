```python
from revenexx.client import Client
from revenexx.services.pages import Pages

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages = Pages(client)

result = pages.pages_templates_list(
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc', # optional
    id = '', # optional
    label = 'Hero with two teasers', # optional
    description = 'Full-width hero followed by a two-column teaser row.', # optional
    page_bundle = 'standard', # optional
    field_name = 'content', # optional
    is_default = True, # optional
    created_by = '', # optional
    created_at = '', # optional
    updated_at = '' # optional
)
```
