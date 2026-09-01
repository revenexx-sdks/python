```python
from revenexx.client import Client
from revenexx.services.pages_editor import PagesEditor
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages_editor = PagesEditor(client)

result: Error = pages_editor.pages_editor_schedule(
    page_id = '',
    scheduled_at = '2026-01-01T12:00:00Z'
)

print(result.model_dump())
```
