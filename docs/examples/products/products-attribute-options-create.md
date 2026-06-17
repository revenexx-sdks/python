```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.products import Products
from revenexx_revenexx.models import AttributeOptions

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products = Products(client)

result: AttributeOptions = products.products_attribute_options_create(
    attribute_id = '',
    code = '',
    labels = {}, # optional
    position = None, # optional
    swatch = {} # optional
)

print(result.model_dump())
```
