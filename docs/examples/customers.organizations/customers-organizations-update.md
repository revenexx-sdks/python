```python
from revenexx.client import Client
from revenexx.services.customers_organizations import CustomersOrganizations
from revenexx.models import Error
from revenexx.enums import OrganizationStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_organizations = CustomersOrganizations(client)

result: Error = customers_organizations.customers_organizations_update(
    id = '',
    branche = 'Maschinenbau', # optional
    credit_limit = 5000, # optional
    customer_number = 'K-10042', # optional
    delivery_block = True, # optional
    lifecycle_stage = 'customer', # optional
    name = 'Beispiel Industrietechnik GmbH', # optional
    payment_terms = 'net_30', # optional
    price_list = 'standard', # optional
    settings = {
        "account_manager": "sales-north",
        "delivery_tour": "tuesday",
        "self_pickup": True
    }, # optional
    status = OrganizationStatus.ACTIVE, # optional
    vat_id = 'DE123456789' # optional
)

print(result.model_dump())
```
