```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.prices import Prices
from revenexx_revenexx.models import PriceEntry
from revenexx_revenexx.enums import PriceEntryType

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

prices = Prices(client)

result: PriceEntry = prices.prices_entries_update(
    list_id = '',
    id = '',
    metadata = {}, # optional
    price_type = PriceEntryType.STANDARD, # optional
    product_id = '', # optional
    quantity_min = None, # optional
    sku = '', # optional
    unit = '', # optional
    unit_price = None, # optional
    valid_from = '', # optional
    valid_until = '' # optional
)

print(result.model_dump())
```
