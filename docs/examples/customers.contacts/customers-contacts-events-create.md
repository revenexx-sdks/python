```python
from revenexx.client import Client
from revenexx.services.customers_contacts import CustomersContacts
from revenexx.models import Error
from revenexx.enums import ContactActivityKind

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_contacts = CustomersContacts(client)

result: Error = customers_contacts.customers_contacts_events_create(
    contact_id = '',
    subject = 'Called about the annual requirement',
    actor = 'vertrieb@example.com', # optional
    kind = ContactActivityKind.NOTE, # optional
    note = 'Asked for a quote on the annual bolt requirement; call back in week 34.', # optional
    occurred_at = '2026-01-01T12:00:00Z' # optional
)

print(result.model_dump())
```
