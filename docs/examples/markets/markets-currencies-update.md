```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.markets import Markets
from revenexx_revenexx.models import MarketCurrency

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

markets = Markets(client)

result: MarketCurrency = markets.markets_currencies_update(
    market_id = '',
    id = '',
    code = '', # optional
    is_default = None, # optional
    position = None # optional
)

print(result.model_dump())
```
