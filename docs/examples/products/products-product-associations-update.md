```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.products import Products
from revenexx_revenexx.models import ProductAssociations

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products = Products(client)

result: ProductAssociations = products.products_product_associations_update(
    id = '',
    association_type_id = '', # optional
    position = None, # optional
    product_id = '', # optional
    quantity = None, # optional
    target_product_id = '' # optional
)

print(result.model_dump())
```
