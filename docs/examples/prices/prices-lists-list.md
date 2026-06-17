```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.prices import Prices

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

prices = Prices(client)

result = prices.prices_lists_list()
```
