```python
from revenexx.client import Client
from revenexx.services.products_categories import ProductsCategories
from revenexx.enums import Source

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products_categories = ProductsCategories(client)

result = products_categories.products_product_categories_list(
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc', # optional
    id = '', # optional
    product_id = '', # optional
    category_id = '', # optional
    position = 1, # optional
    source = Source.MANUAL, # optional
    created_at = '2026-01-01T12:00:00Z' # optional
)
```
