```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.markets import Markets
from revenexx_revenexx.models import MarketContext

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

markets = Markets(client)

result: MarketContext = markets.markets_context(
    id = ''
)

print(result.model_dump())
```
