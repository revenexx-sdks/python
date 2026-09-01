```python
from revenexx.client import Client
from revenexx.services.pages import Pages
from revenexx.models import SeedResult

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages = Pages(client)

result: SeedResult = pages.pages_seed(
    menus = [], # optional
    pages = [] # optional
)

print(result.model_dump())
```
