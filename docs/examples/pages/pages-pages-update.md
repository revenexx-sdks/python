```python
from revenexx.client import Client
from revenexx.services.pages import Pages
from revenexx.models import Error
from revenexx.enums import PageStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages = Pages(client)

result: Error = pages.pages_pages_update(
    id = '',
    bundle = 'standard', # optional
    meta = {}, # optional
    slug = 'about-us', # optional
    status = PageStatus.DRAFT, # optional
    title = 'About us' # optional
)

print(result.model_dump())
```
