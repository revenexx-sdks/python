```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.markets import Markets
from revenexx_revenexx.models import MarketTaxClass

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

markets = Markets(client)

result: MarketTaxClass = markets.markets_tax_classes_create(
    market_id = '',
    code = '',
    name = '',
    is_default = None, # optional
    labels = {}, # optional
    position = None, # optional
    rate = None # optional
)

print(result.model_dump())
```
