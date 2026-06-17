```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.prices import Prices
from revenexx_revenexx.models import PriceEntry

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

prices = Prices(client)

result: PriceEntry = prices.prices_entries_get(
    list_id = '',
    id = ''
)

print(result.model_dump())
```
