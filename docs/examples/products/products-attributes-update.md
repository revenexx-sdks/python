```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.products import Products
from revenexx_revenexx.models import Attributes

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products = Products(client)

result: Attributes = products.products_attributes_update(
    id = '',
    code = '', # optional
    config = {}, # optional
    entity_ref = '', # optional
    entity_type = '', # optional
    group_id = '', # optional
    is_filterable = None, # optional
    is_unique = None, # optional
    labels = {}, # optional
    localizable = None, # optional
    position = None, # optional
    scopable = None, # optional
    type = '', # optional
    usable_in_grid = None, # optional
    validation = {} # optional
)

print(result.model_dump())
```
