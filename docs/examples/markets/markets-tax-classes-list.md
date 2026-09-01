```python
from revenexx.client import Client
from revenexx.services.markets import Markets
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

markets = Markets(client)

result: Error = markets.markets_tax_classes_list(
    market_id = '',
    id = '', # optional
    code = 'standard', # optional
    name = 'Standard rate', # optional
    labels = '{"de-DE":"Regelsatz","en-GB":"Standard rate"}', # optional
    rate = 20, # optional
    is_default = True, # optional
    position = 0, # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z', # optional
    limit = 50, # optional
    offset = 0, # optional
    order = 'position.asc' # optional
)

print(result.model_dump())
```
