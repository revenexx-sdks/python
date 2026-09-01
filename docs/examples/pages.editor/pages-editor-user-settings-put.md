```python
from revenexx.client import Client
from revenexx.services.pages_editor import PagesEditor

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages_editor = PagesEditor(client)

result = pages_editor.pages_editor_user_settings_put(
    settings = {} # optional
)
```
