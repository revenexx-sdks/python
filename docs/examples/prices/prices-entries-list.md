```python
from revenexx.client import Client
from revenexx.services.prices import Prices
from revenexx.models import Error
from revenexx.enums import PriceEntryType

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

prices = Prices(client)

result: Error = prices.prices_entries_list(
    list_id = '',
    id = '', # optional
    product_id = '', # optional
    sku = 'BOLT-M8-30', # optional
    price_type = PriceEntryType.STANDARD, # optional
    quantity_min = 9.99, # optional
    unit_price = 9.99, # optional
    unit = 'pcs', # optional
    valid_from = '2026-01-01T12:00:00Z', # optional
    valid_until = '2026-01-01T12:00:00Z', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z', # optional
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc' # optional
)

print(result.model_dump())
```
