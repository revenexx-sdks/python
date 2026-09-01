```python
from revenexx.client import Client
from revenexx.services.inventories_locations import InventoriesLocations
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

inventories_locations = InventoriesLocations(client)

result: Error = inventories_locations.inventories_locations_delete(
    id = ''
)

print(result.model_dump())
```
