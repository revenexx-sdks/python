```python
from revenexx.client import Client
from revenexx.services.customers_contacts import CustomersContacts
from revenexx.models import Error
from revenexx.enums import CustomersContactsCreateRegistrationStatus
from revenexx.enums import ContactStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_contacts = CustomersContacts(client)

result: Error = customers_contacts.customers_contacts_create(
    email = 'einkauf@example.com',
    first_name = 'Anna', # optional
    is_primary = True, # optional
    job_title = 'Einkaufsleitung', # optional
    last_name = 'Berger', # optional
    locale = 'de-DE', # optional
    order_approval_limit = 25000, # optional
    organization_id = '', # optional
    phone = '+49 30 5550123', # optional
    registration_status = CustomersContactsCreateRegistrationStatus.PENDING, # optional
    role = 'buyer', # optional
    status = ContactStatus.INVITED # optional
)

print(result.model_dump())
```
