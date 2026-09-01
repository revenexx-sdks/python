```python
from revenexx.client import Client
from revenexx.services.pages_delivery import PagesDelivery
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

pages_delivery = PagesDelivery(client)

result: Error = pages_delivery.pages_delivery_page(
    slug = 'about-us', # optional
    id = '', # optional
    langcode = 'de' # optional
)

print(result.model_dump())
```
