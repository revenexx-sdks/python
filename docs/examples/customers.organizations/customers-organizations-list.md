```python
from revenexx.client import Client
from revenexx.services.customers_organizations import CustomersOrganizations
from revenexx.enums import CustomersOrganizationsListStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_organizations = CustomersOrganizations(client)

result = customers_organizations.customers_organizations_list(
    id = '', # optional
    name = 'Beispiel Industrietechnik GmbH', # optional
    vat_id = 'DE123456789', # optional
    branche = 'Maschinenbau', # optional
    customer_number = 'K-10042', # optional
    status = CustomersOrganizationsListStatus.ACTIVE, # optional
    lifecycle_stage = 'customer', # optional
    payment_terms = 'net_30', # optional
    credit_limit = 9.99, # optional
    price_list = 'standard', # optional
    delivery_block = True, # optional
    external_team_id = '', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z', # optional
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc' # optional
)
```
