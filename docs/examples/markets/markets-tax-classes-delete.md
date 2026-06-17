```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.markets import Markets

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

markets = Markets(client)

result = markets.markets_tax_classes_delete(
    market_id = '',
    id = ''
)
```
