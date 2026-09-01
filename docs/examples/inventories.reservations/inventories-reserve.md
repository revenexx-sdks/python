```python
from revenexx.client import Client
from revenexx.services.inventories_reservations import InventoriesReservations
from revenexx.models import Error
from revenexx.models import InventoryStockItem

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

inventories_reservations = InventoriesReservations(client)

result: Error = inventories_reservations.inventories_reserve(
    order_ref = 'SO-2026-000123',
    expires_at = '2026-01-01T12:00:00Z', # optional
    items = [InventoryStockItem()], # optional
    location_code = 'main', # optional
    product_id = '', # optional
    quantity = 2, # optional
    ship_to = {}, # optional
    sku = 'ACME-4711-BLK' # optional
)

print(result.model_dump())
```
