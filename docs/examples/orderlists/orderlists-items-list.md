```python
from revenexx.client import Client
from revenexx.services.orderlists import Orderlists
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

orderlists = Orderlists(client)

result: Error = orderlists.orderlists_items_list(
    list_id = '',
    id = '', # optional
    product_id = '', # optional
    sku = 'ACME-4711-BLK', # optional
    name = 'Copy paper A4, 80 g/m², white', # optional
    image = 'https://cdn.example.com/catalog/acme-4711-blk.jpg', # optional
    quantity = 12, # optional
    unit = 'piece', # optional
    price = 3.49, # optional
    tax_rate = 19, # optional
    cost_center_id = 'CC-100', # optional
    position_texts = '{}', # optional
    custom_sku = 'CUST-4711', # optional
    category_slug = 'office-supplies', # optional
    subcategory_slug = 'paper', # optional
    position = 0, # optional
    metadata = '{}', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z', # optional
    limit = 50, # optional
    offset = 0, # optional
    order = 'created_at.desc' # optional
)

print(result.model_dump())
```
