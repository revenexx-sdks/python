```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.customers import Customers
from revenexx_revenexx.models import Address
from revenexx_revenexx.enums import AddressType

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers = Customers(client)

result: Address = customers.customers_addresses_update(
    id = '',
    city = '', # optional
    company = '', # optional
    contact_id = '', # optional
    country = '', # optional
    is_default = None, # optional
    name = '', # optional
    organization_id = '', # optional
    phone = '', # optional
    region = '', # optional
    street = '', # optional
    street2 = '', # optional
    type = AddressType.BILLING, # optional
    zip = '' # optional
)

print(result.model_dump())
```
