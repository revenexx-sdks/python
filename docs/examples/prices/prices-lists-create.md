```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.prices import Prices
from revenexx_revenexx.models import PriceList
from revenexx_revenexx.enums import PriceListStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

prices = Prices(client)

result: PriceList = prices.prices_lists_create(
    code = '',
    name = '',
    channel_id = '', # optional
    contact_id = '', # optional
    currency = '', # optional
    description = '', # optional
    is_default = None, # optional
    labels = {}, # optional
    market_id = '', # optional
    metadata = {}, # optional
    organization_id = '', # optional
    priority = None, # optional
    status = PriceListStatus.ACTIVE, # optional
    tax_included = None, # optional
    valid_from = '', # optional
    valid_until = '' # optional
)

print(result.model_dump())
```
