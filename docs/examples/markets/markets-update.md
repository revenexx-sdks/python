```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.markets import Markets
from revenexx_revenexx.models import Market
from revenexx_revenexx.enums import MarketStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

markets = Markets(client)

result: Market = markets.markets_update(
    id = '',
    code = '', # optional
    currency = '', # optional
    is_default = None, # optional
    labels = {}, # optional
    name = '', # optional
    position = None, # optional
    status = MarketStatus.ACTIVE # optional
)

print(result.model_dump())
```
