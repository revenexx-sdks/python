```python
from revenexx.client import Client
from revenexx.services.products import Products

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products = Products(client)

result = products.products_product_associations_list(
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc', # optional
    id = '', # optional
    product_id = '', # optional
    association_type_id = '', # optional
    target_product_id = '', # optional
    quantity = 9.99, # optional
    position = 1, # optional
    created_at = '2026-01-01T12:00:00Z' # optional
)
```
