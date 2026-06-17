```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.inventories import Inventories
from revenexx_revenexx.models import Location
from revenexx_revenexx.enums import LocationType

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

inventories = Inventories(client)

result: Location = inventories.inventories_locations_update(
    id = '',
    address = {}, # optional
    code = '', # optional
    enabled = None, # optional
    labels = {}, # optional
    metadata = {}, # optional
    name = '', # optional
    priority = None, # optional
    type = LocationType.WAREHOUSE # optional
)

print(result.model_dump())
```
