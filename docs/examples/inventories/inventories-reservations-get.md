```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.inventories import Inventories
from revenexx_revenexx.models import Reservation

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

inventories = Inventories(client)

result: Reservation = inventories.inventories_reservations_get(
    id = ''
)

print(result.model_dump())
```
