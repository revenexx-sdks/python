```python
from revenexx.client import Client
from revenexx.services.markets import Markets
from revenexx.models import Error
from revenexx.enums import MarketStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

markets = Markets(client)

result: Error = markets.markets_create(
    code = 'northwind',
    name = 'Northwind',
    currency = 'EUR', # optional
    is_default = False, # optional
    labels = {
        "de-DE": "Nordwind",
        "en-GB": "Northwind"
    }, # optional
    position = 0, # optional
    status = MarketStatus.ACTIVE # optional
)

print(result.model_dump())
```
