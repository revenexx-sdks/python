```python
from revenexx.client import Client
from revenexx.services.inventories_stock import InventoriesStock
from revenexx.models import InventoryVocabularyIndex

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

inventories_stock = InventoriesStock(client)

result: InventoryVocabularyIndex = inventories_stock.inventories_vocabularies_list()

print(result.model_dump())
```
