```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.inventories import Inventories
from revenexx_revenexx.models import StockLevel

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

inventories = Inventories(client)

result: StockLevel = inventories.inventories_stock_update(
    id = '',
    location_id = '', # optional
    metadata = {}, # optional
    on_hand = None, # optional
    product_id = '', # optional
    reorder_point = None, # optional
    reserved = None, # optional
    sku = '' # optional
)

print(result.model_dump())
```
