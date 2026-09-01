```python
from revenexx.client import Client
from revenexx.services.products import Products
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products = Products(client)

result: Error = products.products_vocabularies_get(
    name = 'product-kinds'
)

print(result.model_dump())
```
