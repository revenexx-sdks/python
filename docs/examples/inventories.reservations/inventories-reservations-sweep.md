```python
from revenexx.client import Client
from revenexx.services.inventories_reservations import InventoriesReservations
from revenexx.models import ReservationSweepResult

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

inventories_reservations = InventoriesReservations(client)

result: ReservationSweepResult = inventories_reservations.inventories_reservations_sweep(
    data = {}
)

print(result.model_dump())
```
