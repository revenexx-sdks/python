```python
from revenexx.client import Client
from revenexx.services.inventories_reservations import InventoriesReservations
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

inventories_reservations = InventoriesReservations(client)

result: Error = inventories_reservations.inventories_release(
    order_ref = 'SO-2026-000123'
)

print(result.model_dump())
```
