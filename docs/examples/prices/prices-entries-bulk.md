```python
from revenexx.client import Client
from revenexx.services.prices import Prices
from revenexx.models import Error
from revenexx.models import PriceEntryReplaceItem
from revenexx.enums import PriceEntriesBulkMode

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

prices = Prices(client)

result: Error = prices.prices_entries_bulk(
    list_id = '',
    entries = [PriceEntryReplaceItem()],
    mode = PriceEntriesBulkMode.UPSERT # optional
)

print(result.model_dump())
```
