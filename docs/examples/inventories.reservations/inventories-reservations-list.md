```python
from revenexx.client import Client
from revenexx.services.inventories_reservations import InventoriesReservations
from revenexx.models import Error
from revenexx.enums import InventoriesReservationsListStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

inventories_reservations = InventoriesReservations(client)

result: Error = inventories_reservations.inventories_reservations_list(
    limit = 50, # optional
    offset = 0, # optional
    order = 'created_at.desc', # optional
    id = '', # optional
    location_id = '', # optional
    product_id = '', # optional
    sku = 'ACME-4711-BLK', # optional
    quantity = 2, # optional
    order_ref = 'SO-2026-000123', # optional
    status = InventoriesReservationsListStatus.ACTIVE, # optional
    expires_at = '2026-01-01T12:00:00Z', # optional
    metadata = '{}', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z' # optional
)

print(result.model_dump())
```
