```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.pages import Pages
from revenexx_revenexx.models import Page
from revenexx_revenexx.enums import PageStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages = Pages(client)

result: Page = pages.pages_pages_update(
    id = '',
    bundle = '', # optional
    meta = {}, # optional
    slug = '', # optional
    status = PageStatus.DRAFT, # optional
    title = '' # optional
)

print(result.model_dump())
```
