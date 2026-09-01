```python
from revenexx.client import Client
from revenexx.services.products import Products
from revenexx.enums import Kind

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

products = Products(client)

result = products.products_list(
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc', # optional
    id = '', # optional
    sku = 'ACME-4711-BLK', # optional
    kind = Kind.SIMPLE, # optional
    parent_id = '', # optional
    family_id = '', # optional
    family_variant_id = '', # optional
    enabled = True, # optional
    tax_class = 'standard', # optional
    attribute_values = '{}', # optional
    label = 'Akku-Bohrschrauber 18V', # optional
    quantified_associations = '{}', # optional
    completeness = '{}', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z', # optional
    deleted_at = '2026-01-01T12:00:00Z' # optional
)
```
