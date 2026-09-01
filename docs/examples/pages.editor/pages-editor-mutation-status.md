```python
from revenexx.client import Client
from revenexx.services.pages_editor import PagesEditor
from revenexx.models import MutationResponse

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages_editor = PagesEditor(client)

result: MutationResponse = pages_editor.pages_editor_mutation_status(
    page_id = '',
    enabled = True,
    index = 1,
    langcode = 'de' # optional
)

print(result.model_dump())
```
