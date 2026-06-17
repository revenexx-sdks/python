```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.pages import Pages
from revenexx_revenexx.models import Menu

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages = Pages(client)

result: Menu = pages.pages_menus_upsert(
    label = '',
    menu_key = '',
    items = [] # optional
)

print(result.model_dump())
```
