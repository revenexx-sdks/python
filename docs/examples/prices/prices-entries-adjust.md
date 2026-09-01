```python
from revenexx.client import Client
from revenexx.services.prices import Prices
from revenexx.models import Error
from revenexx.enums import PriceEndingRule

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

prices = Prices(client)

result: Error = prices.prices_entries_adjust(
    list_id = '',
    amount = 9.99, # optional
    dry_run = True, # optional
    percent = 9.99, # optional
    rounding = PriceEndingRule.EXACT, # optional
    sku_prefix = 'BOLT-' # optional
)

print(result.model_dump())
```
