```python
from revenexx.client import Client
from revenexx.services.customers_organizations import CustomersOrganizations
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_organizations = CustomersOrganizations(client)

result: Error = customers_organizations.customers_addresses_update(
    id = '',
    city = 'Berlin', # optional
    company = 'Beispiel Industrietechnik GmbH', # optional
    contact_id = '', # optional
    country = 'DE', # optional
    is_default = True, # optional
    name = 'Anna Berger', # optional
    organization_id = '', # optional
    phone = '+49 30 5550123', # optional
    region = 'Berlin', # optional
    street = 'Musterstraße 12', # optional
    street2 = 'Gebäude C, 2. OG', # optional
    type = 'shipping', # optional
    zip = '10115' # optional
)

print(result.model_dump())
```
