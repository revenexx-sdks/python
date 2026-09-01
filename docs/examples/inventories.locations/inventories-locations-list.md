```python
from revenexx.client import Client
from revenexx.services.inventories_locations import InventoriesLocations
from revenexx.models import Error
from revenexx.enums import InventoriesLocationsListType

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

inventories_locations = InventoriesLocations(client)

result: Error = inventories_locations.inventories_locations_list(
    limit = 50, # optional
    offset = 0, # optional
    order = 'created_at.desc', # optional
    id = '', # optional
    code = 'main', # optional
    name = 'Main warehouse', # optional
    labels = '{}', # optional
    type = InventoriesLocationsListType.WAREHOUSE, # optional
    priority = 0, # optional
    enabled = True, # optional
    address = '{}', # optional
    metadata = '{}', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z' # optional
)

print(result.model_dump())
```
