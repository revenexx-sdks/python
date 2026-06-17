```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.products import Products
from revenexx_revenexx.models import FamilyAttributes

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products = Products(client)

result: FamilyAttributes = products.products_family_attributes_update(
    id = '',
    attribute_id = '', # optional
    family_id = '', # optional
    is_required = None, # optional
    position = None, # optional
    required_channels = {} # optional
)

print(result.model_dump())
```
