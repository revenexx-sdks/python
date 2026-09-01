```python
from revenexx.client import Client
from revenexx.services.inventories_stock import InventoriesStock
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

inventories_stock = InventoriesStock(client)

result: Error = inventories_stock.inventories_stock_adjust(
    id = '',
    quantity = -3,
    reason = 'Stocktake 2026-03, two units damaged' # optional
)

print(result.model_dump())
```
