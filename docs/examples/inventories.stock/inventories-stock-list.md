```python
from revenexx.client import Client
from revenexx.services.inventories_stock import InventoriesStock
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

inventories_stock = InventoriesStock(client)

result: Error = inventories_stock.inventories_stock_list(
    limit = 50, # optional
    offset = 0, # optional
    order = 'created_at.desc', # optional
    id = '', # optional
    location_id = '', # optional
    product_id = '', # optional
    sku = 'ACME-4711-BLK', # optional
    on_hand = 42, # optional
    reserved = 5, # optional
    reorder_point = 10, # optional
    metadata = '{}', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z' # optional
)

print(result.model_dump())
```
