```python
from revenexx.client import Client
from revenexx.services.pages_editor import PagesEditor
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages_editor = PagesEditor(client)

result: Error = pages_editor.pages_editor_templates_create(
    page_id = '',
    label = 'Hero with two teasers',
    uuids = [],
    description = 'Full-width hero followed by a two-column teaser row.', # optional
    field_name = 'content', # optional
    is_default = True, # optional
    page_bundle = 'standard' # optional
)

print(result.model_dump())
```
