```python
from revenexx.client import Client
from revenexx.services.pages_editor import PagesEditor
from revenexx.models import MutationResponse

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages_editor = PagesEditor(client)

result: MutationResponse = pages_editor.pages_editor_take_ownership(
    page_id = ''
)

print(result.model_dump())
```
