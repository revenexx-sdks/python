```python
from revenexx.client import Client
from revenexx.services.products import Products
from revenexx.models import Error
from revenexx.enums import Kind

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products = Products(client)

result: Error = products.products_grid(
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc', # optional
    q = 'cordless drill', # optional
    kind = Kind.SIMPLE, # optional
    enabled = True, # optional
    family_id = '' # optional
)

print(result.model_dump())
```
