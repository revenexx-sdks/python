```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.pages import Pages
from revenexx_revenexx.models import MutationResponse

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages = Pages(client)

result: MutationResponse = pages.pages_editor_mutation_status(
    page_id = '',
    enabled = None,
    index = None,
    langcode = '' # optional
)

print(result.model_dump())
```
