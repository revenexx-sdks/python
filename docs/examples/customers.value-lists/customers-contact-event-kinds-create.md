```python
from revenexx.client import Client
from revenexx.services.customers_value_lists import CustomersValueLists
from revenexx.models import Error
from revenexx.enums import Tone

client = Client()
client.set_endpoint('https://api.revenexx.com') # Your API Endpoint
client.set_api_key_auth('<API_KEY>') # A gateway-managed scoped API key (rvxk_…).

customers_value_lists = CustomersValueLists(client)

result: Error = customers_value_lists.customers_contact_event_kinds_create(
    code = '',
    title = 'Phone call',
    description = 'Somebody spoke to this person on the phone.', # optional
    descriptions = {
        "de": "Es wurde mit dieser Person telefoniert.",
        "en": "Somebody spoke to this person on the phone."
    }, # optional
    is_default = True, # optional
    labels = {
        "de": "Telefonat",
        "en": "Phone call"
    }, # optional
    position = 1, # optional
    tone = Tone.NEUTRAL # optional
)

print(result.model_dump())
```
