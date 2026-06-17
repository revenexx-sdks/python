```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.products import Products
from revenexx_revenexx.models import Products as ProductsModel

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products = Products(client)

result: ProductsModel = products.products_update(
    id = '',
    attribute_values = {}, # optional
    completeness = {}, # optional
    deleted_at = '', # optional
    enabled = None, # optional
    family_id = '', # optional
    family_variant_id = '', # optional
    kind = '', # optional
    parent_id = '', # optional
    quantified_associations = {}, # optional
    sku = '', # optional
    tax_class = '' # optional
)

print(result.model_dump())
```
