```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.customers import Customers
from revenexx_revenexx.models import Organization
from revenexx_revenexx.enums import OrganizationStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers = Customers(client)

result: Organization = customers.customers_organizations_update(
    id = '',
    name = '', # optional
    settings = {}, # optional
    status = OrganizationStatus.ACTIVE, # optional
    vat_id = '' # optional
)

print(result.model_dump())
```
