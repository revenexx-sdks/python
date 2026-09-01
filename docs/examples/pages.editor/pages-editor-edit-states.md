```python
from revenexx.client import Client
from revenexx.services.pages_editor import PagesEditor
from revenexx.enums import PageEditStateStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages_editor = PagesEditor(client)

result = pages_editor.pages_editor_edit_states(
    status = PageEditStateStatus.ACTIVE, # optional
    limit = 1, # optional
    offset = 1 # optional
)
```
