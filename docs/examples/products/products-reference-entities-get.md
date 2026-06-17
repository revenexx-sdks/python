```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.products import Products
from revenexx_revenexx.models import ReferenceEntities

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products = Products(client)

result: ReferenceEntities = products.products_reference_entities_get(
    id = ''
)

print(result.model_dump())
```
