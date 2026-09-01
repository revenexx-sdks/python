```python
from revenexx.client import Client
from revenexx.services.inventories_locations import InventoriesLocations
from revenexx.models import Error
from revenexx.enums import LocationType

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

inventories_locations = InventoriesLocations(client)

result: Error = inventories_locations.inventories_locations_create(
    code = 'main',
    name = 'Main warehouse',
    address = {
        "city": "Nuremberg",
        "country": "DE",
        "postal_code": "90402",
        "street": "Industriering 4"
    }, # optional
    enabled = True, # optional
    labels = {
        "de": "Hauptlager",
        "en": "Main warehouse"
    }, # optional
    metadata = {
        "erp_site": "1000"
    }, # optional
    priority = 0, # optional
    type = LocationType.WAREHOUSE # optional
)

print(result.model_dump())
```
