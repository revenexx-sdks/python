```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.pages import Pages

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages = Pages(client)

result = pages.pages_menus_list()
```
