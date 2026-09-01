```python
from revenexx.client import Client
from revenexx.services.markets import Markets
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

markets = Markets(client)

result: Error = markets.markets_tax_classes_update(
    market_id = '',
    id = '',
    code = 'standard', # optional
    is_default = True, # optional
    labels = {
        "de-DE": "Regelsatz",
        "en-GB": "Standard rate"
    }, # optional
    name = 'Standard rate', # optional
    position = 0, # optional
    rate = 20 # optional
)

print(result.model_dump())
```
