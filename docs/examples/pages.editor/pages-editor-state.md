```python
from revenexx.client import Client
from revenexx.services.pages_editor import PagesEditor
from revenexx.models import EditorState

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages_editor = PagesEditor(client)

result: EditorState = pages_editor.pages_editor_state(
    page_id = '',
    langcode = 'de', # optional
    index = 1 # optional
)

print(result.model_dump())
```
