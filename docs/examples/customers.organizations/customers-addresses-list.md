```python
from revenexx.client import Client
from revenexx.services.customers_organizations import CustomersOrganizations

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_organizations = CustomersOrganizations(client)

result = customers_organizations.customers_addresses_list(
    id = '', # optional
    organization_id = '', # optional
    contact_id = '', # optional
    type = 'shipping', # optional
    company = 'Beispiel Industrietechnik GmbH', # optional
    name = 'Anna Berger', # optional
    street = 'Musterstraße 12', # optional
    street2 = 'Gebäude C, 2. OG', # optional
    zip = '10115', # optional
    city = 'Berlin', # optional
    region = 'Berlin', # optional
    country = 'DE', # optional
    phone = '+49 30 5550123', # optional
    is_default = True, # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z', # optional
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc' # optional
)
```
