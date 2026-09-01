```python
from revenexx.client import Client
from revenexx.services.customers_contacts import CustomersContacts

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_contacts = CustomersContacts(client)

result = customers_contacts.customers_contact_events_list(
    id = '', # optional
    contact_id = '', # optional
    organization_id = '', # optional
    kind = 'call', # optional
    name = 'activity.call', # optional
    subject = 'Called about the annual requirement', # optional
    actor = 'vertrieb@example.com', # optional
    occurred_at = '2026-01-01T12:00:00Z', # optional
    created_at = '2026-01-01T12:00:00Z', # optional
    limit = 1, # optional
    offset = 1, # optional
    order = 'created_at.desc' # optional
)
```
