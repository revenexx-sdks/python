```python
from revenexx.client import Client
from revenexx.services.prices import Prices
from revenexx.models import Error
from revenexx.models import PriceResolveItem

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

prices = Prices(client)

result: Error = prices.prices_resolve(
    items = [PriceResolveItem()],
    at = '2026-03-15T09:00:00Z', # optional
    channel_id = '', # optional
    contact_id = '', # optional
    currency = 'EUR', # optional
    market_id = '', # optional
    organization_id = '' # optional
)

print(result.model_dump())
```
