```python
from revenexx.client import Client
from revenexx.services.pages import Pages
from revenexx.models import Error
from revenexx.models import PageMenuItem

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages = Pages(client)

result: Error = pages.pages_menus_upsert(
    label = 'Main navigation',
    menu_key = 'main',
    items = [PageMenuItem()] # optional
)

print(result.model_dump())
```
