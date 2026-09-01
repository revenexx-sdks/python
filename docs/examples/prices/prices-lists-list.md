```python
from revenexx.client import Client
from revenexx.services.prices import Prices
from revenexx.models import Error
from revenexx.enums import PriceListStatus
from revenexx.enums import PriceListTaxBasis

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

prices = Prices(client)

result: Error = prices.prices_lists_list(
    id = '', # optional
    code = 'standard', # optional
    name = 'Standard prices', # optional
    description = 'The list every buyer falls back to.', # optional
    currency = 'EUR', # optional
    status = PriceListStatus.ACTIVE, # optional
    priority = 1, # optional
    is_default = True, # optional
    tax_basis = PriceListTaxBasis.NET, # optional
    tax_included = True, # optional
    requires_auth = True, # optional
    contact_id = '', # optional
    organization_id = '', # optional
    channel_id = '', # optional
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
