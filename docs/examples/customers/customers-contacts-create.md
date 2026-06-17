```python
from revenexx_revenexx.client import Client
from revenexx_revenexx.services.customers import Customers
from revenexx_revenexx.models import Contact
from revenexx_revenexx.enums import ContactRole
from revenexx_revenexx.enums import ContactStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers = Customers(client)

result: Contact = customers.customers_contacts_create(
    email = '',
    first_name = '', # optional
    is_primary = None, # optional
    last_name = '', # optional
    locale = '', # optional
    organization_id = '', # optional
    phone = '', # optional
    role = ContactRole.BUYER, # optional
    status = ContactStatus.INVITED # optional
)

print(result.model_dump())
```
