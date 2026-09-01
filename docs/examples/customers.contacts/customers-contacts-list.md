```python
from revenexx.client import Client
from revenexx.services.customers_contacts import CustomersContacts
from revenexx.enums import Status
from revenexx.enums import RegistrationStatus

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_contacts = CustomersContacts(client)

result = customers_contacts.customers_contacts_list(
    id = '', # optional
    organization_id = '', # optional
    email = 'einkauf@example.com', # optional
    first_name = 'Anna', # optional
    last_name = 'Berger', # optional
    phone = '+49 30 5550123', # optional
    job_title = 'Einkaufsleitung', # optional
    role = 'buyer', # optional
    status = Status.INVITED, # optional
    order_approval_limit = 9.99, # optional
    registration_status = RegistrationStatus.PENDING, # optional
    registration_decided_at = '2026-01-01T12:00:00Z', # optional
    registration_decided_by = 'vertrieb@example.com', # optional
    registration_reason = 'Could not be verified as a commercial buyer.', # optional
    locale = 'de-DE', # optional
    is_primary = True, # optional
    external_user_id = '', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    updated_at = '2026-01-01T12:00:00Z', # optional
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc' # optional
)
```
