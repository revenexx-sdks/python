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

result: Error = prices.prices_lists_update(
    id = '',
    channel_id = '', # optional
    code = 'dealer-de', # optional
    contact_id = '', # optional
    currency = 'EUR', # optional
    description = 'Contract prices for authorised dealers.', # optional
    is_default = True, # optional
    labels = {
        "de": "H\u00e4ndlerpreise",
        "en": "Dealer prices"
    }, # optional
    metadata = {
        "erp_price_group": "A1",
        "source_system": "erp"
    }, # optional
    name = 'Dealer prices', # optional
    organization_id = '', # optional
    priority = 1, # optional
    requires_auth = True, # optional
    status = PriceListStatus.ACTIVE, # optional
    tax_basis = PriceListTaxBasis.NET, # optional
    tax_included = True, # optional
    valid_from = '2026-01-01T00:00:00Z', # optional
    valid_until = '2026-12-31T23:59:59Z' # optional
)

print(result.model_dump())
```
