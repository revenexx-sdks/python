```python
from revenexx.client import Client
from revenexx.services.markets import Markets
from revenexx.models import Error
from revenexx.enums import MarketStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

markets = Markets(client)

result: Error = markets.markets_clone(
    id = 'northwind',
    code = 'northwind-b2b',
    copy_currencies = True, # optional
    copy_locales = True, # optional
    copy_tax_classes = True, # optional
    currency = 'EUR', # optional
    name = 'Northwind B2B', # optional
    status = MarketStatus.ACTIVE # optional
)

print(result.model_dump())
```
