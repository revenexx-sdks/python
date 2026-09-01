```python
from revenexx.client import Client
from revenexx.services.prices import Prices
from revenexx.models import Error
from revenexx.enums import PriceEndingRule

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

prices = Prices(client)

result: Error = prices.prices_entries_ladder(
    list_id = '',
    base_price = 9.99,
    discount_percent = 9.99, # optional
    product_id = '', # optional
    quantities = [1,10,50], # optional
    replace = True, # optional
    rounding = PriceEndingRule.EXACT, # optional
    sku = 'BOLT-M8-30', # optional
    unit = 'pcs' # optional
)

print(result.model_dump())
```
