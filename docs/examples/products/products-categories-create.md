```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.products import Products
from revenexx_revenexx.models import Categories

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products = Products(client)

result: Categories = products.products_categories_create(
    code = '',
    labels = {}, # optional
    parent_id = '', # optional
    path = '', # optional
    position = None, # optional
    values = {} # optional
)

print(result.model_dump())
```
