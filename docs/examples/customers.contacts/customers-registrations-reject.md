```python
from revenexx.client import Client
from revenexx.services.customers_contacts import CustomersContacts
from revenexx.models import Error

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_contacts = CustomersContacts(client)

result: Error = customers_contacts.customers_registrations_reject(
    contact_id = '',
    reason = 'Could not be verified as a commercial buyer.',
    decided_by = 'vertrieb@example.com' # optional
)

print(result.model_dump())
```
